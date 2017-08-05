#第一版
'''

while True:
    lucky_num=19
    input_num=int(input("input the guess numn:"))

    if input_num==lucky_num:
        print("bingo!")
        break
    elif input_num>lucky_num:
        print("the real numer is smaller.")
    else:
        print("the real num is bigger..")

'''
lucky_num=19
input_num=-1
while lucky_num!=input_num:
    input_num=int(input("input the guess numn:"))
    if input_num>lucky_num:
        print("the real numer is smaller.")
    elif input_num<lucky_num:
        print("the real num is bigger..")
print("bingo!")
