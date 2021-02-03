import os
import time
os.system('cls')
print('''
###### Happy Birthday Wisher ######
This is a program to wish your friend on his/her Birthday ######
''')
time.sleep(3)
os.system('cls')
f=input("From: ")
t=input("To: ")
age=input("Enter the age of the birthday boy/girl: ")
os.system('cls')
print(f'''
Happy birthday, {t}. 
I would have made today a public holiday because you are a rare breed but let’s leave that for another day. 
To my one and only, you deserve the blessings showered on you and many other benefits that God will unleash on you. 
Smile today and every other day of your life on earth.
From the one crazy friend named {f}. Wish you a happy Birthday again
''')
time.sleep(1)
print('''
Woww!!! You have grown ...
''')
time.sleep(1)
i=0
while(i<len(age)):
    file=age[i]+".txt"
    with open(f"{file}") as f:
        ag=f.read()
    print(ag+"\n")
    i+=1
    time.sleep(1)
print('''years old.''')
with open("cake.txt") as f:
    cake=f.read()
time.sleep(1)
print(cake)