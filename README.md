<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <img src="https://github.com/WStudioGroup/hifumi-plugins/blob/main/remove.photos-removed-background.png" width="200">
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-better-broadcast

_✨ 将你的信息广播到所有群聊，支持多种类型 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/captain-wangrun-cn/nonebot-plugin-better-broadcast.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-better-broadcast">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-better-broadcast.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>

## 📖 介绍

将你的信息广播到所有群聊，支持多种类型

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-better-broadcast

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-better-broadcast
</details>


打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_better_broadcast"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项          | 类型   | 必填 | 默认值 | 说明                  |
|:------------:|:----:|:---:|:---:|:-------------------:|
| bc_blacklist | list | 否  | [ ]  | 群聊黑名单，广播时将不会发送到这些群聊 |
| bc_random_delay | bool | 否  | 是  | 随机延迟，发送广播时将会有随机1-3秒的延迟 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 发送广播 | 主人 | 否 | 私聊、群聊 | 顾名思义 |
| 撤回广播 | 主人 | 否 | 私聊、群聊 | 撤回上一条广播的消息 |
### 效果图
<img src="imgs/QQ20241109-123325.png">
<img src="imgs/QQ20241109-123336.png">

## 📃 更新日志
### 1.0.6（2025.01.01）
- 🍟修复了一些问题
### 1.0.5（2025.01.01）
- 🍟修复了一些问题
### 1.0.4（2024.11.15）
- 🧋添加了“撤回广播”指令和取消广播，更改了插件信息
