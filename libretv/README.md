# JellyView直播订阅

第02版 · 主流覆盖与特色精选。发布日期2026-11-03；视频与网页检查日期2026-10-31。接替[第01版](../docs/feeds/01-首版资料说明.md)。

## 直接使用

| 列表 | 视频 | 独立网页 | 订阅与配置 |
| --- | ---: | ---: | --- |
| 默认精选 | 204 | 139 | [M3U](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/LibreTV-HD-Only.m3u)／[JSON](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/LibreTV-HD-Only.json) |
| 扩充备选 | 34 | 0 | [M3U](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/JellyView-Expansion.m3u)／[JSON](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/JellyView-Expansion.json) |

在“添加直播源”中填M3U地址，或在支持配置导入的客户端粘贴JSON。配置中的地址与台标均使用公网URL，无需运行本机服务。`JellyView-Selected.m3u`是默认精选的同内容别名，不必重复添加；两个精选JSON都指向原来的固定地址，便于去重。

本模块衔接[LibreTV](https://github.com/LibreSpark/LibreTV)的M3U订阅及LibreTV-SourceList配置方式；JSON的`liveSources`供LibreTV读取，`live`供JellyView读取。普通M3U播放器可读取基础频道和台标；分层分类与网页入口需相应客户端支持。

## 当前范围

| 地区／国家 | 精选视频 | 独立官网入口 | 扩充视频 |
| --- | ---: | ---: | ---: |
| 中国大陆 | 51 | 0 | 0 |
| 中国香港 | 6 | 9 | 0 |
| 中国台湾 | 7 | 16 | 0 |
| 美国 | 25 | 13 | 4 |
| 俄罗斯 | 16 | 11 | 9 |
| 英国 | 18 | 12 | 7 |
| 加拿大 | 13 | 11 | 1 |
| 德国 | 18 | 11 | 3 |
| 法国 | 16 | 13 | 5 |
| 意大利 | 23 | 7 | 5 |
| 日本 | 2 | 20 | 0 |
| 韩国 | 9 | 16 | 0 |

精选：137路1080P、2路2160P、21路720P–1080P浮动、44路720P。扩充：20路1080P、14路720P。10月31日最终238条视频线路的最新两次短时检查均通过解码和清单推进；发布日不重复声称已测流，记录不保证跨网络或全天稳定。

大陆51路身份和顺序保留，修复CCTV-10、河南卫视和河北卫视的播放线路。港台与海外按八类筛选，同类主流台并列，再补特色台，不为凑齐分类或数量而混淆频道版本。

139个官网入口不计入视频画质；10月31日页面检查中121项可达，18项受限或未确认，未逐站登录或测网页视频。17路暂缓直连不在精选、扩充订阅里。

[导入与台标](../docs/feeds/02-订阅导入与台标说明.md) · [精选清单](../docs/feeds/02-204路精选频道清单.md) · [扩充清单](../docs/feeds/02-34路扩充频道清单.md) · [分类和官网](../docs/feeds/02-分类覆盖与官网入口.md) · [画质说明](../docs/checks/02-画质与可用性说明.md) · [版本索引](../docs/feeds/00-版本索引.md)
