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

#第二版
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
'''
# lucky_num=19
# input_num=-1
# guess_count=0;
# while lucky_num!=input_num and guess_count<3:
#     input_num=int(input("input the guess numn:"))
#     if input_num>lucky_num:
#         print("the real numer is smaller.")
#     elif input_num<lucky_num:
#         print("the real num is bigger..")
#     else:
#         print("bingo!")
#     guess_count+=1
# else:
#     print("Too many retrys !!")

lucky_num=19
input_num=-1
guess_count=0;
while  guess_count<3:
    input_num=int(input("input the guess numn:"))
    if input_num>lucky_num:
        print("the real numer is smaller.")
    elif input_num<lucky_num:
        print("the real num is bigger..")
    else:
        print("bingo!")
        break
    guess_count+=1
else:
    print("Too many retrys !!")