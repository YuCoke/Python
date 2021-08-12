import qrcode
import xlrd
import os

# 输入文件路径
fileName = input("请输入文件地址名称")
# 打开文件
work = xlrd.open_workbook(fileName)
print(work.sheet_names())
sheet1 = work.sheets()[1]
rows = sheet1.nrows
print("共有", sheet1.ncols, "列")
# 输入要使用的数据列'
fName = sheet1.col_values(0)
datas = sheet1.col_values(1)
path = sheet1.col_values(2)
i = 0
f = open('target.txt', 'a', encoding='utf-8')
while i < len(fName):
    data = datas[i]
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    if data.strip() == '':
        msg = fName[i]
        f.write(msg + "\n")
        i += 1
    else:
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        imgName = str(fName[i]) + '.png'
        img.save(os.path.join(path[1], imgName))
        i += 1
else:
    print('共有', i)

