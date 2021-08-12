# coding: utf-8
import xlrd
import os

# 输入文件路径
# path = input("请输入该文件路径")
fileName = input("请输入文件地址名称")
# 打开文件
work = xlrd.open_workbook(fileName)
print(work.sheet_names())
sheet1 = work.sheets()[0]
rows = sheet1.nrows
print("共有", sheet1.ncols, "列")
num = int(input('请输入要使用的数据列'))
coln = sheet1.col_values(num-1)


renamePath = input('要重命名文件地址')
# 获取所有需要重命名文件名字
renameList = os.listdir(renamePath)
i = 0

while i < len(renameList) | i < len(coln):
    os.rename(os.path.join(renamePath, renameList[i]), os.path.join(renamePath, str(coln[i]) + '.docx'))
    i += 1


