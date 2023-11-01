# README

市场情绪周期数据指标可视化项目，包含多个观察指标。

特别注意，以下几个包含密码的配置文件不允许提交到代码仓库：
- 1、config.ini 包含了数据库地址、用户名、数据库登陆密码、网站登陆密码等信息

本项目常用的部署命令：
  - 构建镜像：```docker build -t short_term_indicator:v1.7 .```
  - 导出镜像: ```docker save -o short_term_indicator_v_1_7.tar imageID```
  - 云服务器导入镜像：```docker load -i short_term_indicator_v_1_7.tar```
  - 给镜像打标签：```docker tag imageID TARGET_IMAGE[:TAG] ```
  - 查看容器：```docker ps```
  - 停止容器：```docker stop containerID```
  - 删除容器：```docker rmi -f containerID```
  - 运行容器：```docker run -d -i -p 5001:5001 imageID```
  - 修改容器名：```docker rename containerID short_term_indicator```


## 部分效果展示

整体效果：
![整体效果](./img/screen_1_update.png)

部分指标：
![市场综合强度](./img/screen_2.png)
![近三日市场综合强度](./img/screen_3.png)
![指数情绪周期图](./img/screen_6.png)
![指数情绪（精确到分）](./img/screen_7.png)
![连板高度](./img/screen_4.png)
![历史封板率](./img/screen_5.png)
