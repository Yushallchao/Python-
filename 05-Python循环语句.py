lucky_num = 28

count = 0
while count<3:
    in_num = int(input("input your guess num:"))

    if in_num==lucky_num:
        print("bingo!")
        break
    elif in_num > lucky_num:
        print("guess num is bigger!")
    else:
        print("guess num is smaller!")
    count+=1
#while … else 循环条件正常结束，执行
else:
    print("count out!")