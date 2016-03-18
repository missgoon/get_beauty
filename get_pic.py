# -*- coding: utf-8 -*-
#!/usr/bin/python3

import requests

def get_pic(save_path,image_url):
  '''
    根据给定的地址下载并保存到本地文件中
  '''
  if len(save_path) == 0 or len(image_url) == 0: return Flase
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