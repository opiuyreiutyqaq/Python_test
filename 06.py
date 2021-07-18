import random

num = int(input("Plz input a number from [0,50]: "))
ans = random.randint(0, 50)
min_num = 0
max_num = 50 

while(ans!=num):
    if(num>ans):
        max_num = num
    else:
        min_num = num
    num = int(input("Plz input a number from [%d,%d]: " % (min_num, (max_num))))


print("Congratulations! the ans is: %d" % (ans))
