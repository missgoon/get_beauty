#!/usr/bin/python
#coding=utf-8

from sys import path
path.append("/root/get_beauty")
import base_func
import redis
import time

count=1
db=redis.StrictRedis(host="139.129.45.40",port=6379,db=0)
while count!=0:
  try:
    image_info=base_func.get_url(count)
    if db.get(image_info[0])==-1: base_func.get_pic("/root/pictures/%s"%image_info[0],image_info[1])
  except:
  	pass
  finally:
    count+=1  

