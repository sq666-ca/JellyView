# JellyView

JellyView汇集客户端软件与配套资源。**当前先提供直播订阅、中文频道分类和画质复测资料**；软件源码与发行资料整理接入中，后续继续沿用本仓库结构。

直播模块结合[LibreTV开源项目](https://github.com/LibreSpark/LibreTV)的订阅接入方式，提供M3U列表与兼容JSON配置，供JellyView以及支持相应格式的LibreTV版本使用。

## 开始使用

- **[M3U直播订阅](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/LibreTV-HD-Only.m3u)**：复制地址，添加到客户端的直播列表。
- **[JSON配置](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/LibreTV-HD-Only.json)**：复制完整内容到支持此格式的配置导入框，或填写该配置地址。
- [完整导入说明](docs/feeds/01-导入与分类说明.md) · [直播模块](libretv/README.md)。

## 当前直播资料

**第01版 · 主流优先与分类扩充 · 2026-10-28**。新仓库首版，没有上一公开版。

当前收录**243路视频**和**69个独立官网入口**。画质记录为1080P及以上174路、720P–1080P浮动7路、720P 62路。港台及海外192路有本轮检查记录，其中191路取得正常节目样本；ARD德国一台部分节目地区受限。中国大陆51路保留原记录，CCTV-10继续标为台标待核。

中国大陆频道按央视、卫视浏览；中国香港频道、中国台湾频道使用八个内容分类。海外频道依次按美国、俄罗斯、英国、加拿大、德国、法国、意大利、日本、韩国排列，再分综合、新闻、动漫、电影、剧集、纪录片、综艺、音乐。每个地区／国家、每类最多4个独立频道，优先主流机构与不同节目库。

英国Most Haunted灵异纪实保留1080P线路，加拿大HauntTV继续收录。单节目专台、混合内容、画质浮动及国际／地区版本分别注明。完整分类界面依客户端实现；资料发布不代表软件已经完成层级适配。

[243路频道清单](docs/feeds/01-243路频道清单.md) · [分类覆盖](docs/feeds/01-分类覆盖与缺口.md) · [节目及媒体背景](docs/feeds/01-243路节目与机构背景.md) · [画质复测报告](docs/checks/01-243路画质与复测说明.md) · [版本索引](docs/feeds/00-版本索引.md)

## 仓库目录

```text
apps/jellyview/       后续软件源码入口
libretv/feeds/        固定地址的M3U和JSON订阅
libretv/catalog/      频道、分类和状态资料
docs/                使用说明、版本索引及复测记录
assets/              后续截图与图标
scripts/feeds/       订阅生成脚本
```

源码与发行资料接入后补充软件使用、开发及下载入口；直播模块继续使用当前固定订阅路径。[文档目录](docs/README.md)提供完整阅读顺序。
