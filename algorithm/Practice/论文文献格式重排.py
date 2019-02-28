def input_my(str):
    res = ''
    while not res:
        res = input(str)
    return res


while True:
    name = input_my("输入作者")
    title = input_my("文章名")
    j = input_my("期刊名")
    year = input_my("年份")
    vol = input_my("卷")
    time = input_my("期")
    page = input_my("page")
    print(name + " " + title + "[J]." + " "+ j + ","
          + year + "," + vol + ",("+time+"): "+page+".")



