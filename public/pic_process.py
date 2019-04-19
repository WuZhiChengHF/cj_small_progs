#!/bin/python3

import os
import base64
import traceback as tbk
#import aa

class pic_proc:
    _pic_src_addr = ""
    _pic_dst_addr = ""
    _py_name      = ""

    def __init__(self, srcaddr, dstaddr="", pic_name=""):
        if srcaddr == "": exit(-1)
        self._pic_src_addr = srcaddr

        if dstaddr == "":
            pos = srcaddr.rfind(".")
            if pos == -1: exit(-1)
            self._pic_dst_addr = srcaddr[:pos+1]+"py"
        else:
            self._pic_dst_addr = dstaddr

        #如果文件不存在,则创建文件
        if not os.path.exists(self._pic_dst_addr):
            os.system(r"touch {}".format(self._pic_dst_addr))

        if pic_name == "":
            pos1 = srcaddr.rfind("/")
            pos2 = srcaddr.rfind(".")
            if pos1 == -1:
                self._py_name = "base64_str_"+srcaddr[:pos2]
            else:
                self._py_name = "base64_str_"+srcaddr[pos1+1:pos2]
        else:
            self._py_name = pic_name

    def pic2py(self):
        try:
            with open(self._pic_src_addr,'rb') as fr, open(self._pic_dst_addr, 'w') as fw:
                strs = base64.b64encode(fr.read()).decode()
                #print(strs.decode())
                if strs != "":
                    pair_str = str(self._py_name)+"="+"\'"+str(strs)+"\'"
                    #pair_str.replace("=b", "=")
                    fw.write(pair_str)
                    return True
                return False
        except:
            tbk.print_exc()
            print("pic to py failed")
            return False

    def _proc_file(self):
        try:
            with open(self._pic_dst_addr, "a") as fw:
                pass
        except:
            print("process file failed")

    def parse_test(self):
        try:
            with open("./test.jpg", 'wb') as fw:
                fw.write(base64.b64decode(aa.base64_str_aa))
                print("parse success ... ")
        except:
            print("parse failed ... ")
 

if '__main__' == __name__:
    p = pic_proc("./cj_pic.png")
    p.pic2py()
    #print(aa.base64_str)
    #p.parse_test()
