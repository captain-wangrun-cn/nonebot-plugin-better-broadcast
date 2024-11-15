import json
from nonebot import on_command, require, get_plugin_config, logger
from nonebot.plugin import PluginMetadata
from nonebot.permission import SUPERUSER
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Bot,Message
require("nonebot_plugin_waiter")
from nonebot_plugin_waiter import waiter
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="更好的广播",
    description="将你的信息广播到所有群聊，支持多种类型",
    usage="发送",
    type="application",
    homepage="https://github.com/captain-wangrun-cn/nonebot-plugin-better-broadcast",
    config=Config,
    supported_adapters={"~onebot.v11"},
)

plugin_config = get_plugin_config(Config)
last_bc_msg_id = []     # 上一条广播的消息id
bc = on_command("发送广播", aliases={"广播","发送群聊广播","广播所有群聊"}, block=True, permission=SUPERUSER)
recall_bc = on_command("撤回广播", block=True, permission=SUPERUSER)

@bc.handle()
async def _(bot: Bot):
    await bc.send("请发送需要广播的内容（发送“取消”以取消）：")

    @waiter(waits=["message"], keep_session=True)
    async def check(event: Event):
        return (event.get_message(),json.loads(event.json()))
    
    msg,data = await check.wait(timeout=120)
    if msg is None:
        await bc.finish("啊哦！输入超时了，请重试")
    if msg.extract_plain_text() == "取消":
        await bc.finish("已取消~")

    forward_msg: bool = data["message"][0]["type"] == "forward"   # 是否为聊天记录

    group_list = await bot.get_group_list()
    blacklist = plugin_config.bc_blacklist
    fail,success = 0,0
    for group in group_list:
        gid = group["group_id"]
        if str(gid) not in blacklist:
            # 不在黑名单内，发送消息
            try:
                if forward_msg:
                    # 聊天记录
                    await bot.forward_group_single_msg(group_id=gid, message_id=data["message_id"])
                else:
                    # 其他消息
                    msg_id = (await bot.send_group_msg(group_id=gid, message=msg))["message_id"]
                    last_bc_msg_id.append(msg_id)    # 记录群聊对应的消息id，便于使用指令撤回
                success += 1
            except Exception as ex:
                # 发送失败
                logger.error(ex)
                fail += 1


    await bc.finish(f"广播完毕！\n成功发送了{success}个群\n有{fail}个群发送失败")


@recall_bc.handle()
async def _(bot: Bot):
    await recall_bc.send("确定要尝试撤回上一条广播吗？（“确认”或“取消”）：")

    @waiter(waits=["message"], keep_session=True)
    async def check(event: Event):
        return event.get_plaintext()

    resp = await check.wait(timeout=120)
    if resp is None:
        await bc.finish("啊哦！输入超时了，请重试")
    if resp == "确认":
        fail,success = 0,0
        for msg_id in last_bc_msg_id:
            try:
                await bot.delete_msg(message_id=msg_id)
                success += 1
            except Exception as ex:
                # 撤回失败
                logger.error(ex)
                fail += 1
        
        await bc.finish(f"已尝试撤回广播\n成功撤回了{success}个群聊\n有{fail}个群撤回失败（可能是因为已经超时）")


    await bc.finish("已取消~")
