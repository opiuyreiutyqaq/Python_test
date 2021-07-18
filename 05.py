import random

users = input("input Rock, Paper, Scissors: ")

rand_num = random.randint(0, 2)
a = ["Rock", "Paper", "Scissors"]

print("Computer: " + a[rand_num])
if(users == a[rand_num]):
    print("Tie!")
elif((users == "Rock" and a[rand_num] == "Scissors") or
     (users == "Paper" and a[rand_num] == "Rock") or
     (users == "Scissors" and a[rand_num] == "Paper")):
    print("You win!")
else: print("You lose!")
