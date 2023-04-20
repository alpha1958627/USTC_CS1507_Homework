import os.path
import random
import re
import time

from utils import *
import bs4
import numpy as np
import pandas as pd
from akshare.stock.cons import hk_js_decode
from py_mini_racer import py_mini_racer
from tqdm.contrib import tzip
import heapq

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from akshare import stock_zh_a_hist
# import akshare as ak
from tqdm import *
from pywebio.output import put_html

from pyecharts import options as opts
from pyecharts.charts import Map, Page, Bar, Line, Kline, Grid
from pyecharts.commons.utils import JsCode

url = 'http://stuhome.ustc.edu.cn/main.htm'
url_yuanxi = 'http://stuhome.ustc.edu.cn/2314/list.htm'#院系传真

news=get_news(url)
print_news(news)
news_yuanxi=get_news(url_yuanxi)
print('\n院系传真\n')
print_news_yuanxi(news_yuanxi)