#!/usr/bin/python
#coding=utf-8

from sys import path
path.append("/root/get_beauty")
import base_func
import redis
import time

db=redis.StrictRedis(host="139.129.45.40",port=6379,db=0)
def runner1():
  while True:
    try:
      image_info=base_func.get_url(db.incr("curr_cursor"))
      if db.get(image_info[0])==-1: base_func.get_pic("/root/pictures/%s"%image_info[0],image_info[1])
    except:
    	pass
    finally:
    	pass

def runner2():
  while True:
    print("ok")
    try:
      stock_info=base_func.get_stock(db.incr("curr_stock_cursor"))
      if db.get(stock_info[0])==-1: db.set(stock_info[0],stock_info[1])
    except:
      pass
    finally:
      pass

if __name__ == '__main__':
  runner2()


