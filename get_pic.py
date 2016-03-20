#!/usr/bin/python
#coding=utf-8

import requests

def get_pic(save_path,iamge_url):
  '''
    根据给定的地址下载并保存到本地文件中
  '''
  image_url="http://static.yidianzixun.com/beauty/imgs/i_000N0FBg.jpg"
  save_path="i_000N0FBg.jpg"
  if len(save_path)==0 or len(image_url)==0: return False
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
