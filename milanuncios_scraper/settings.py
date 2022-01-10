# -*- coding: utf-8 -*-

# Scrapy settings for milanuncios_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'milanuncios_scraper'

SPIDER_MODULES = ['milanuncios_scraper.spiders']
NEWSPIDER_MODULE = 'milanuncios_scraper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'milanuncios_scraper.middlewares.MilanunciosScraperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'milanuncios_scraper.middlewares.MilanunciosScraperDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'milanuncios_scraper.pipelines.MilanunciosScraperPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408, 405]
RETRY_TIMES = 1
DOWNLOAD_TIMEOUT = 30

DOWNLOADER_MIDDLEWARES = {
   # 'realestate.middlewares.RealestateDownloaderMiddleware': 543,
   #  'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
   #  'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350
   'scrapy_crawlera.CrawleraMiddleware': 610,
   #  'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
   #  'scrapy_proxies.RandomProxy': 100,
   #  'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
   'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
   'random_useragent.RandomUserAgentMiddleware': 400
}
PROXY_LIST = 'proxies.txt'
PROXY_MODE = 0
USER_AGENT_LIST = "user-agents.txt"

CRAWLERA_ENABLED = True
CRAWLERA_PRESERVE_DELAY = True
CRAWLERA_APIKEY = '09246d7e58834ac1913d79ce988c2178'