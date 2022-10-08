import pandas
with open("nato_phonetic_alphabet.csv") as data:
    phonetic_alphabet=pandas.read_csv(data)


nato_phonetic_alphabet=pandas.DataFrame(phonetic_alphabet)

data_dic={row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

word=(input("enter a word\n").replace(" ","")).upper()
list_letters=[letter for letter in word]
is_there_an_error=True
while is_there_an_error:
    try:
        list_letters = [letter for letter in word]
        result=[data_dic[letter] for letter in list_letters]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        word = (input("enter a word\n").replace(" ", "")).upper()
    else:
        break

print(result)