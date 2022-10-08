from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"
def word_transfomer(s):
    if s=="NOUN":
        return random_noun()
    elif s=="VERB":
        return random_verb()
    else:
        return s[0]

def process_madlib(mad_lib):
    processed = ""
    while mad_lib!="" :
        if mad_lib[0:4]=="NOUN":
            processed+=word_transfomer("NOUN")
            mad_lib=mad_lib[4:]
        if mad_lib[0:4]=="VERB":
            processed+=word_transfomer("VERB")
            mad_lib=mad_lib[4:]
        if mad_lib[0:4]!="NOUN" and mad_lib[0:4]!="VERB":
            processed+=mad_lib[0]
            mad_lib=mad_lib[1:]
    return processed
print(process_madlib("I'm going to VERB to the store and pick up a NOUN or two."))








