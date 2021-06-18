# news_spider
新闻类爬虫

### Scrapy 
1. scrapy startproject news_spider
2. cd news_spider
3. scrapy genspider baidu_hot top.baidu.com/buzz?b=1
4. scrapy crawl baidu_hot

### 安装
1. python3.7
2. centos7
4. virtualenv vens --python=python3
3. pip install -r requirements.txt

### 部署
1.部署scrapyd
- supervisord -c supervisor.conf
- supervisorctl -c supervisor.conf

2.测试是否成功
- curl http://127.0.0.1:6800/listversions.json?project=news_spider
- curl http://localhost:6800/schedule.json -d project=default -d spider=baidu  
