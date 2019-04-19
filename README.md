# cj_small_progs

## 将图片base64编码命令 
- cat cj_pic.png | base64 > cj_pic.py 

## 编译选项
- cd dict_compare
- pyinstaller.exe -F -w  dict_match.py xls_process.py cj_pic.py pic_gen.py

## pip 安装 
- pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
