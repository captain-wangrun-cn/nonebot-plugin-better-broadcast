import nonebot,json
from nonebot import on_command, require
from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot.permission import SUPERUSER
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Bot,Message,MessageSegment
require("nonebot_plugin_waiter")
from nonebot_plugin_waiter import waiter
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_better_broadcast",
    description="将你的信息广播到所有群聊，支持多种类型",
    usage="【指令前缀】广播",
    type="application",
    homepage="https://github.com/captain-wangrun-cn/nonebot-plugin-better-broadcast",
    config=Config,
    supported_adapters={"~onebot.v11"},
)

plugin_config = get_plugin_config(Config)
bc = on_command("发送广播", aliases={"广播","发送群聊广播","广播所有群聊"}, block=True, permission=SUPERUSER)

@bc.handle()
async def _(bot: Bot):
    await bc.send("请发送需要广播的内容（支持多种格式）：")

    @waiter(waits=["message"], keep_session=True)
    async def check(event: Event):
        return (event.get_message(),json.loads(event.json()))
    
    msg,data = await check.wait(timeout=120)
    if msg is None:
        await bc.finish("啊哦！输入超时了，请重试")

    forward_msg: bool = data["message"][0]["type"] == "forward"   # 是否为聊天记录

    group_list = await bot.get_group_list()
    blacklist = plugin_config.bc_blacklist
    fail,success = 0,0
    for i in group_list:
        gid = i["group_id"]
        if str(gid) not in blacklist:
            # 不在黑名单内，发送消息
            try:
                if forward_msg:
                    # 聊天记录
                    await bot.forward_group_single_msg(group_id=gid, message_id=data["message_id"])
                else:
                    # 其他消息
                    await bot.send_group_msg(group_id=gid, message=msg)
                success += 1
            except:
                # 发送失败
                fail += 1


    await bc.finish(f"广播完毕！\n成功发送了{success}个群\n有{fail}个群发送失败")
