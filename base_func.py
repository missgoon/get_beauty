#!/usr/bin/python
#coding=utf-8

import requests
import os

def get_pic(save_path,iamge_url):
  '''
    根据给定的地址下载并保存到本地文件中
  '''
  image_url="http://static.yidianzixun.com/beauty/imgs/i_000N0FBg.jpg"
  save_path="i_000N0FBg.jpg"
  if len(save_path)==0 or len(image_url)==0: return False
  if not os.path.exists(r"/root/get_beauty/%s"%save_path): print("creating a file %s\n"%save_path);os.system(r"touch %s"%save_path)
  response=requests.get(image_url,stream=True)
  image=response.content
  print("begining save image %s...\n"%save_path)
  try:
    with open(save_path,"wb") as file:
      file.write(image)
      return True
  except IOError:
   print("IO Error\n")
   return False
  finally:
    file.close

def get_url(num):
  '''
    从根据得到的num，访问网址http://www.yidianzixun.com/api/q/?path=channel|news-list-for-channel&channel_id=u241&fields=up&cstart=1&cend=2
    并从中得到图片的名称和地址
  '''
  url="http://www.yidianzixun.com/api/q/?path=channel|news-list-for-channel&channel_id=u241&fields=up&cstart=%d&cend=%d"%(num,num+1)
  response=requests.get(url)
  a_str=(response.content).split('"channel_image":"')
  image_url="".join(a[1].strip("\}").strip('\"').split("\\"))
  print(image_url)