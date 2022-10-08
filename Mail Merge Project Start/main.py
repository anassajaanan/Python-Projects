#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"./Input/Names/invited_names.txt") as file:
    list_names=file.read().splitlines()

with open(r"./Input/Letters/starting_letter.txt") as letter:
    starting_letter=letter.read()



for name in list_names:
    new_latter=starting_letter.replace("[name]", name)

    with open(r"./Output/ReadyToSend/letter_for_"+f"{name}"".txt", mode="w") as letter_to_send:
        letter_to_send.write(new_latter)