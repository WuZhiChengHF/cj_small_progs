#!/usr/bin/python3
#coding: utf-8
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as fdi
import re
from xls_process import *
import pic_gen as pgen
import cj_pic as cj

compare_dict = {}
pg = pgen.pic_proc()

def fpath_choice(flag):
    filename = fdi.askopenfilename()
    if filename != "":
        if flag == "index":
            #pass#index_text.insert(0, filename)
            index_e.set(filename)
        elif flag == "value":
            value_e.set(filename)
        elif flag == "add":
            add_e.set(filename)
        elif flag == "add_value":
            add_value_e.set(filename)
        else:
            pass

def summit():
    col_re = re.compile(r'^[a-zA-Z]{1,3}$')
    if col_value.get() == '' or col_index.get() == '' or col_add.get() == '' or \
            not re.match(col_re, col_index.get()) or not re.match(col_re, col_value.get()) or \
            not re.match(col_re, col_add.get()):
        tkinter.messagebox.showinfo("提示", "数据填写错误")
        #print(col_index.get(), col_value.get(), col_add.get())
        col_index.delete(0, END)
        col_value.delete(0, END)
        col_add.delete(0, END)
    else:
        operator_excel()

def operator_excel():
    index_table_name = index_e.get()
    index_sheet_name = sheet_index.get()
    index_col_name = col_index.get()
    compare_key = xls_read_process(index_e.get(), sheet_index.get(), col_index.get())
    compare_value = xls_read_process(value_e.get(), sheet_value.get(), col_value.get())
    add_key = xls_read_process(add_e.get(), sheet_add.get(), col_add.get())
    j=0;
    for i in compare_key:
        if j < len(compare_value):
            compare_dict[i] = compare_value[j];
        else:
            compare_dict[i] = " ";
        j = j+1
    k=0
    value=[]
    for key in add_key:
        if key in compare_dict:
            value.append(compare_dict[key])
        else:
            value.append("none")
        k=k+1
    #print(value)
    ret = xls_write_process(value)
    if ret == 0:
        tkinter.messagebox.showinfo("提示", "./result.txt已生成!")


root = Tk()
#设置窗口的大小宽x高+偏移量
root.geometry('520x250')
#设置窗口标题
root.title('excel处理')
#第0行内容
Label(root, text="文件路径", fg='red').grid(row=0, column=1)
Label(root, text="sheet", fg='red').grid(row=0, column=3, padx=10)
Label(root, text="所在列", fg='red').grid(row=0, column=4, padx=10)
#第一行内容
Label(root, text="索引").grid(row=1, column=0)
index_e = StringVar()
Entry(root, textvariable=index_e).grid(row=1, column=1)
index_e.set("input key filepath...")
Button(text="选择文件", width=6, command=lambda:fpath_choice("index")).grid(row=1, column=2, padx=4)
sheet_index=tkinter.Entry(root, width=6)
sheet_index.grid(row=1, column=3, padx=10)
col_index=tkinter.Entry(root, width=6)
col_index.grid(row=1, column=4, padx=10)
#第二行内容
Label(root, text="对应值").grid(row=2, column=0)
value_e = StringVar()
Entry(root, textvariable=value_e).grid(row=2, column=1)
value_e.set("input value filepath...")
Button(text="选择文件", width=6, command=lambda:fpath_choice("value")).grid(row=2, column=2, padx=4)
sheet_value=Entry(root, width=6)
sheet_value.grid(row=2, column=3, padx=10)
col_value=Entry(root, width=6)
col_value.grid(row=2, column=4, padx=10)
#第三行内容
Label(root, text="关联").grid(row=3, column=0)
add_e = StringVar()
Entry(root, textvariable=add_e).grid(row=3, column=1)
add_e.set("input add filepath...")
Button(text="选择文件", width=6, command=lambda:fpath_choice("add")).grid(row=3, column=2, padx=4)
sheet_add=Entry(root, width=6)
sheet_add.grid(row=3, column=3, padx=10)
col_add=Entry(root, width=6)
col_add.grid(row=3, column=4, padx=10)
##第四行内容
#Label(root, text="添加到").grid(row=4, column=0)
#add_value_e = StringVar()
#Entry(root, textvariable=add_value_e).grid(row=4, column=1)
#add_value_e.set("input add filepath...")
#Button(text="选择文件", width=6, command=lambda:fpath_choice("add_value")).grid(row=4, column=2, padx=4)
#sheet_add_value=Entry(root, width=6)
#sheet_add_value.grid(row=4, column=3, padx=10)
#col_add_value=Entry(root, width=6)
#col_add_value.grid(row=4, column=4, padx=10)

pg.get_pic(cj.base64_str_cj_pic, "./cj_pic.png")
#添加图片
photo = PhotoImage(file="./cj_pic.png")
Label(root, image=photo).grid(row=1, column=5, rowspan=3, padx=5, pady=5)
#添加提交按钮
Button(text="提交", width=10, command=summit).grid(row=5, columnspan=8, pady=20)

if '__main__' == __name__:
    mainloop()

