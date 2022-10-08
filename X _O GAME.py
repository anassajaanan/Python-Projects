from random import randint
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
list=[]
position1 = input("Where do you want to put the treasure? ")
list.append(position1)
vertical1=int(position1[1])-1
horizontal1=int(position1[0])-1
map[vertical1][horizontal1]="❌️"
print(f"{row1}\n{row2}\n{row3}")
computer_number_vertical1=randint(0,2)
computer_number_horizontal1=randint(0,2)
while computer_number_vertical1==vertical1 and computer_number_horizontal1==horizontal1:
    computer_number_vertical1=randint(0,2)
    computer_number_horizontal1=randint(0,2)
position3=str(computer_number_horizontal1+1)+str(computer_number_vertical1+1)
list.append(position3)
# print(list)
# print(f"{row1}\n{row2}\n{row3}")
map[computer_number_vertical1][computer_number_horizontal1]="🔴  "
print(f"{row1}\n{row2}\n{row3}")
position2 = input("Where do you want to put the treasure again? ")
list.append(position2)
vertical2=int(position2[1])-1
horizontal2=int(position2[0])-1
map[vertical2][horizontal2]="❌️"
print(f"{row1}\n{row2}\n{row3}")
computer_number_vertical2=randint(0,2)
computer_number_horizontal2=randint(0,2)
position4=str(computer_number_horizontal2+1)+str(computer_number_vertical2+1)
while position4 in list:
    computer_number_vertical2=randint(0,2)
    computer_number_horizontal2=randint(0,2)
map[computer_number_vertical2][computer_number_horizontal2]="🔴  "
print(f"{row1}\n{row2}\n{row3}")
position5 = input("Where do you want to put the treasure again? ")
vertical5=int(position5[1])-1
horizontal5=int(position5[0])-1

if vertical5==vertical1==vertical2 or horizontal5==horizontal2==horizontal1:
    map[vertical5][horizontal5] = "❌️"
    print(f"{row1}\n{row2}\n{row3}")
    print("you win)")














