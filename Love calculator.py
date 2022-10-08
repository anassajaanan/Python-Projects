# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your wife's name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# lower_name1=name1.lower()
# lower_name2=name2.lower()
# full_name=lower_name2+lower_name1
full_name=(name1+name2).lower()

num1=0
num2=0
for i in range(len("true")):
    for j in range(len(full_name)):
        if "true"[i]==full_name[j]:
            num1+=1
print(num1)
for i in range(len("love")):
    for j in range(len(full_name)):
        if "love"[i]==full_name[j]:
            num2+=1
print(num2)
score=int(str(num1)+str(num2))
if score<10 and score>90:
    print("Your score is", score,"you go together like coke and mentos.")
elif score <50 and score>40:
    print("Your score is", score,", you are alright together.")
else:
    print("Your score is", score)






