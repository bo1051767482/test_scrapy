# 导入cmd方法
from scrapy import  cmdline
# 写出你要运行的指令  nba可被替换为你要爬取的应用名
cmdline.execute('scrapy crawl dianping'.split())

