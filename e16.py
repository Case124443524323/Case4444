import random

ran_number = random.randint(1, 100)
jisu = 0
while True:
    random_suru = int(input("请输入一个数字："))
    jisu += 1
    if random_suru < ran_number:
        print("小了")
    elif random_suru > ran_number:
        print("大了")
    else:
        print("猜对了，总共猜了" + str(jisu) + "次")
        break
    if jisu == 5:
        print("失败了")
        break