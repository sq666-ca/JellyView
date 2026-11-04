# JellyView

JellyView汇集客户端软件与配套资源。**当前先提供直播订阅、中文频道分类和台标资源**；软件源码与发行资料整理接入中，后续继续沿用本仓库结构。

直播模块结合[LibreTV开源项目](https://github.com/LibreSpark/LibreTV)的M3U订阅与LibreTV-SourceList配置方式整理，供JellyView以及支持相应格式的播放器使用。地区分层和官网混排等扩展信息依客户端版本显示。

## 开始使用

- **[精选M3U订阅](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/LibreTV-HD-Only.m3u)**：204路视频，另附139个独立官网网页入口。
- **[精选JSON配置](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/LibreTV-HD-Only.json)**：复制全文到配置导入框，或填写配置地址。已添加同一订阅地址时直接刷新。
- **[扩充M3U](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/JellyView-Expansion.m3u)**／[扩充JSON](https://raw.githubusercontent.com/sq666-ca/JellyView/main/libretv/feeds/JellyView-Expansion.json)：34路独立备选，需要时再添加。

原订阅地址继续有效，无需本机服务。[导入与台标说明](docs/feeds/02-订阅导入与台标说明.md) · [直播模块](libretv/README.md)

## 当前直播资料

**第02版 · 主流覆盖与特色精选 · 发布于2026-11-03，测流记录截至2026-10-31。** 本版接替公开第01版；[版本索引](docs/feeds/00-版本索引.md)区分当前与历史资料。

默认精选204路，扩充34路与精选互不重复。另有139个独立官网入口，17路异常或受限线路暂缓导入。精选画质记录为137路1080P、2路2160P、21路720P–1080P浮动、44路720P。

先收录各地区、各国有代表性的电视机构与频道，同类可并列多家，再补充特色台；不设每类1台或4台上限。中国大陆51路继续按央视、卫视浏览；中国香港频道、中国台湾频道及海外使用综合、新闻、动漫、电影、剧集、纪录片、综艺、音乐。海外先选国家，再选内容类别。

英国真人憨豆、Most Haunted灵异纪实、古董公路之旅，以及加拿大HauntTV继续保留。国际版、地方版、单节目专台与多节目频道保留真实身份。官网是打开方式，不是单独分类；视频已有同台官网操作时不重复列卡片。

全部377个可见条目中371项配有频道或机构识别图，6项保留频道简称资料。具体显示和图片失效回退依客户端支持。画质与可用性反映10月31日短时抽样，发布日未重新测流；官网网页不计为已测视频，也不承诺所有地区或全天稳定。

[精选频道](docs/feeds/02-204路精选频道清单.md) · [扩充频道](docs/feeds/02-34路扩充频道清单.md) · [分类与官网入口](docs/feeds/02-分类覆盖与官网入口.md) · [画质说明](docs/checks/02-画质与可用性说明.md) · [本版更新](docs/feeds/02-主流覆盖与特色精选.md)

## 仓库目录

```text
apps/jellyview/       后续软件源码入口
libretv/feeds/        固定地址的精选、扩充M3U与JSON
libretv/catalog/      频道、分类、选择与台标资料
docs/                按版本编号组织的使用和更新说明
assets/logos/        频道与机构识别图
scripts/feeds/       订阅生成脚本
```

源码与发行资料接入后补充软件使用、开发及下载入口。直播资料编号与软件版本号分开管理。[文档目录](docs/README.md)提供阅读顺序。
