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
# 输入要使用的数据列
fName = sheet1.col_values(0)
dirName = ['产品包装图片', '电商平台二维码', '农产品全过程照片', '品牌包装图片', '品牌标志', '品牌传播视频', '企业网站二维码']

count = 0
for name in fName:
    path = r'D:\10大名品资料整理' + '\\' + name.strip()
    # 判断是否存在
    if not os.path.exists(path):
        os.mkdir(path)
        for pName in dirName:
            dirPath = path + '\\' + pName
            if not os.path.exists(dirPath):
                os.mkdir(dirPath)
    count += 1
print('共：', count)

