#                                   """create mammal file for DOG WHALE CAT"""
import os
filepath = os.path.join(os.getcwd(), 'mammals.txt')
if not os.path.exists(filepath):
    with open(filepath, 'w'):
        pass
    
mammals_name = ['dog','whale','cat']
mammals_sex  = ['female','male']
dog_vac      = ['yes','no']
names        = []
sex          = []
ages         = []
features     = []

numbers = input("How many mammals from [DOG WHALE CAT] list would you like to have in your own list?\n")
for i in range(int(numbers)):
    temp = input("What is the mammal name?\n1:dog / 2:whale / 3:cat\n")
    names.append(mammals_name[int(temp)-1])
    temp = input("What is the mammal sex?\nChoose from 1:female / 2:male\n")
    sex.append(mammals_sex[int(temp)-1])
    temp = input("How old is it?\n")
    ages.append(int(temp))
    if names[i] == 'dog':
        temp = input("Has the dog vaccinated? 1:yes or 2:no?\n")
        features.append(dog_vac[int(temp)-1])
    else:
        temp = input("Enter the Cat: birthplace or Whale: livingplace\n")
        features.append(temp)
    with open(filepath, "a") as f:
        f.write("%s %s %d %s\n" % (names[i],sex[i],ages[i],features[i]))

