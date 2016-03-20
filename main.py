#!/usr/bin/python
#coding=utf-8

from sys import path
path.append("/root/get_beauty")
import base_func

count=0
while count<10000:
  try:
    image_info=base_func.get_url(count)
    base_func.get_pic("/root/pictures/%s"%image_info[0],image_info[1])
  except:
  	pass
  finally:
    count+=1  

