#import 在這裡
from __future__ import unicode_literals

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys as key
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from urllib.request import urlretrieve

import time, re, sys, random, os

from function_ import *
from data_ import *