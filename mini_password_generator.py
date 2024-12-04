import random
def pass_generator():
    l=["@","#","%","&"]
    upper=chr(random.randint(65,90))
    lower=chr(random.randint(97,122))
    special=random.choice(l)
    digit=random.randint(10000,99999)
    character=upper+lower+special+str(digit)
    return character
    

result=pass_generator()
print(result)
