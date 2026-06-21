# App-only 推荐插件阻塞说明

这些插件 manifest 中 `skills_count=0`、`apps_count>0`，没有本地 Skill 可读；必须依赖 app connector 工具暴露和账号授权。

| 插件 | apps_count | 本轮状态 | 阻塞原因 |
| --- | ---: | --- | --- |
| `readwise` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `scite` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `amplitude` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `mixpanel` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `similarweb` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `brand24` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `dovetail` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `jam` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `mem` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `semrush` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
| `datadog` | 11 | 已安装但未实际读取业务数据 | 当前线程未暴露 app connector 工具；需要授权/新线程工具可见后再跑 |
