# -*- coding: utf-8 -*-  
'''
Created on 2013-7-24

@author: chenxiaguang
python processURL -U "http://xxxx" -R "referencexxx"
拿到flasshgot获取到的url 
同时获取剪切板上的内容 做为标题
并写入文件
'''

import argparse
import win32clipboard
import win32con
import ConfigParser
import time
# import win32cons

def getClipboardText():  
    win32clipboard.OpenClipboard()  
    result = win32clipboard.GetClipboardData(win32con.CF_TEXT)  
    win32clipboard.CloseClipboard()  
    return result

#python processURL -U "http://xxxx" -R "referencexxx"
parser = argparse.ArgumentParser(description = 'Process the URL of download attached files.')
parser.add_argument('-U', type=str, default='', dest='URL', help='The URL of Download attached files.')
parser.add_argument('-R', type=str, default='', dest='referenceURL', help='The URL of Download attached files.')
args = parser.parse_args()
fileURL = args.URL
referenceURL = args.referenceURL

#title 来自剪切板
title = getClipboardText()
title = title.replace(",", "_");
title = title.replace("#", "_");
currentTime = time.strftime('#%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))

# 解析配置文件 获得文件保存路径
config=ConfigParser.ConfigParser()
config.readfp(open("./cfg.ini","rb"))
saveFile = config.get("global", "saveFilePath");


# raw_input('>>')
# 追加写入文件
writeContent = currentTime + "\n";
writeContent = writeContent + title + "," + fileURL + "," + referenceURL + "\n"

logFile = open(saveFile, 'a')
try:
    logFile.write(writeContent);
finally:
    logFile.close()


