# 订阅生成脚本

在仓库根目录运行`python scripts/feeds/build-feeds.py`，从频道、扩充与台标资料生成两份M3U、两份配置及原固定路径的精选别名。默认输出本仓库的公网Raw地址。

如在其他仓库或静态站点部署，可使用`python scripts/feeds/build-feeds.py --base-url https://example.com/JellyView`，该根地址需同时提供`libretv/feeds/`与`assets/logos/`。脚本不联网、不测流、不改变频道归属，不修改软件或安装器。
