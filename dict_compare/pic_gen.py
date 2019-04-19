#!/usr/bin/python3
#coding: utf-8
import os
import base64
import traceback as tbk
import cj_pic as cj

class pic_proc:
    _pic_addr = ""

    def __init__(self):
        pass

    def get_pic(self, base64str="", dstaddr=""):
        #如果文件不存在,则创建文件
        if not os.path.exists(dstaddr):
            os.system(r"touch {}".format(dstaddr))
        if base64str == "" or dstaddr == "": return False
        try:
            with open(dstaddr, 'wb') as fw:
                fw.write(base64.b64decode(base64str))
                #print("parse success ... ")
        except:
            print("parse failed ... ")
            tbk.print_exc()


if '__main__' == __name__:
    pp = pic_proc()
    pp.get_pic(cj.base64_str_cj_pic, "./cj_pic2.png")

