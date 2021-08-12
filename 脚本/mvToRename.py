import os
import xlrd

# 输入文件路径
fileName = input("请输入文件地址名称")
# 打开文件
work = xlrd.open_workbook(fileName)
print(work.sheet_names())
sheet1 = work.sheets()[0]
rows = sheet1.nrows
print("共有", sheet1.ncols, "列")
# 输入要使用的数据列'
fName = sheet1.col_values(2)
frName = sheet1.col_values(3)
fPath = sheet1.col_values(4)
cName = sheet1.col_values(5)

# 公共路径
sourcePath = r'D:\10大名品源文件'
# sourcePath = r'D:\新建文件夹'

i = 0
num = int(0)
f = open('work/log.txt', 'a', encoding='utf-8')

while i < len(fName):
    # 目标文件绝对地址
    mkPath = sourcePath + '\\' + fName[i]
    if not os.path.exists(mkPath):
        msg = str(i+1) + cName[i] + mkPath + '文件未找到' + "\n"
        f.write(msg)
        num += 1
        i += 1
        continue
    else:
        # 移动路径
        tgPath = fPath[i] + '\\' + str(frName[i])
        # 文件后缀获取
        suffix = os.path.splitext(mkPath)[-1]
        # 移动文件
        os.rename(mkPath, tgPath + suffix)
        # os.rename(fPath[i], frName + suffix)
        i += 1
else:
    print("共完成了数据：", i)
    print("失败了的数据：", num)
    f.close()


