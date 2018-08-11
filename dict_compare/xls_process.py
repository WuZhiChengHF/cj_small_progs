#coding:utf-8
import xlrd, xlwt, xlutils
from xlrd import open_workbook
from xlutils.copy import copy
import os
import time
import datetime

#col_dict={"A":1, "B":2, "C":3, "A":1, "B":2, "C":}

def xls_read_process(xls_table_name, xls_sheet_name, xls_col_name):
    xls_table = xlrd.open_workbook(xls_table_name)
    sheet_rd = xls_table.sheet_by_name(xls_sheet_name)
    i = 0;
    col_index = 0;
    for case in xls_col_name[::-1]:
        if i == 0:
            col_index = col_index + ord(case.upper())-ord('A')
        else:
            col_index = col_index + (26**i)*(ord(case.upper())-ord('A')+1)
        i = i+1;
    #print(col_index)
    column_rd = sheet_rd.col_values(col_index)
    print(column_rd)
    return column_rd

#def xls_write_process(xls_table_name, xls_sheet_name, xls_col_name, str_array):
#    rb = open_workbook(xls_table_name)
#    #通过sheet_by_index()获取的sheet没有write()方法 rs = rb.sheet_by_index(0)
#    wb = copy(rb)
#    #利用xlutils.copy函数，将xlrd.Book转为xlwt.Workbook，再用xlwt模块进行存储
#    #通过get_sheet()获取的sheet有write()方法
#    ws = wb.get_sheet(0)
#    ws.write(0, 0, 'changed!')
#    wb.save(xls_table_name)
#    return 0
def xls_write_process(str_array):
    #f = xlwt.Workbook() #创建工作簿
    #sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    #k=0
    #for i in str_array:
    #    sheet1.write(k, 0, i)
    #    k=k+1
    #f.save('result.xlsx')
    filename="./result_"+time.strftime("%H_%M_%S")+".txt"
    fd=open(filename, 'w')
    try:
        for i in str_array:
            #fd.write(str(k)+i)
            fd.write(str(i)+"\n")
            #k=k+1
    finally:
        fd.close()
    return 0


#if '__main__' == __name__:
#    #xls_read_process("./1.xlsx", "Sheet1", "B")
#    a=['1','2','3']
#    xls_write_process(a)
