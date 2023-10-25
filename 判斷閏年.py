def year(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        print("是閏年")
    else:
        print("不是閏年")

year(int(input("請輸入年份： ")))
