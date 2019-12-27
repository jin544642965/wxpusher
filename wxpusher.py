#coding:utf-8

#description:代码发布微信通知api

#environment: python3

#author: jorden



import requests

import sys

import time

import subprocess

import json



class WXpusher_api:

    """

    describe：代码发布消息通知到微信

    """



    def __init__(self, title, commitid, status):

        self.commitid = commitid

        self.current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        self.proj_name = subprocess.run("git log --pretty=format:\"%%s\" %s -1" % commitid, shell=True, stdout=subprocess.PIPE).stdout.decode("utf8").strip()

        self.author = subprocess.run("git show %s  --pretty=format:\"%%an\"|sed -n 1p" % commitid, shell=True, stdout=subprocess.PIPE).stdout.decode("utf8").strip()

        self.status = status

        self.change_file_list = subprocess.run('git diff --name-only HEAD~ HEAD', shell=True, stdout=subprocess.PIPE).stdout.decode("utf8").strip()

        self.title = title

        self.url = "http://wxpusher.zjiecode.com/api/send/message"

        self.headers = {

                      "content-type":"application/json"

                      }

        self.content = """

**[%s]**  

发布时间: %s  

项目: %s  

发布状态: <font color=red>%s</font>  

发布人: %s  

发布的文件列表: %s

                      """ % (self.title, self.current_time, self.proj_name, self.status, self.author, self.change_file_list)

        





        self.data = {

                    "appToken":"AT_ZnmHbwWYxxxxIEyQni4miU72dcLy43WW",

                    "content": "{0}".format(self.content),

                    "contentType":3,

                    "topicIds":[

                    123

                    ],

                    "uids":[

                    "UID_xxxxxxxxxxxxxxxxxxxxxxx1",

                    "UID_xxxxxxxxxxxxxxxxxxxxxxx2",

                    ],

                    "url":""

                    }





    def send_message(self):

        reps = requests.post(self.url, json=self.data, headers=self.headers).json()

        #print(json.dumps(reps, ensure_ascii=False))







if __name__ == '__main__':

    title = sys.argv[1]

    commitid = sys.argv[2]

    status = sys.argv[3]

    wxpusher = WXpusher_api(title, commitid, status)

    wxpusher.send_message()