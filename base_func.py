#!/usr/bin/python
#coding=utf-8

import requests
import os

def get_pic(save_path,image_url):
  '''
    根据给定的地址下载并保存到本地文件中
  '''
  if len(save_path)==0 or len(image_url)==0: return False
  if os.path.exists(r"/root/pictures/%s"%save_path): return False
  #if not os.path.exists(r"/root/get_beauty/%s"%save_path): print("creating a file %s\n"%save_path);os.system(r"touch %s"%save_path)
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
    http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=美女&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=10&cend=20&version=999999&infinite=true
    并从中得到图片的名称和地址
  '''
  #url="http://www.yidianzixun.com/api/q/?path=channel|news-list-for-channel&channel_id=u241&fields=up&cstart=%d&cend=%d"%(num,num+1)
  url="http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=美女&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=%d&cend=%d&version=999999&infinite=true"%(num,num+1)
  response=requests.get(url)
  a_str=(response.content).split('"image":"')[1].split('"')
  image_url="".join(a_str[0].strip("\}").strip('\"').split("\\"))
  name=image_url.split("/")[-1]
  print("get image info name: %s url:%s"%(name,image_url))
  return [name,image_url]