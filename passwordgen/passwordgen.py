#Script to Create Passwords
import random
import string


print("Creating a Password (Minimum 4 Charachters)")
lenght = int(input("\n Enter the number of Password Charachters \n"))
while lenght < 4:
    lenght = int(input("\n Enter the number of Password Charachters \n"))
if lenght >=4:
    passnum = lenght-4

    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    numbers =  string.digits
    special = string.punctuation
    allposs = upper_case + lower_case + numbers + special
#Minimum Requeriments for a Password

    tempass = random.sample(upper_case,1)
    tempass2 = random.sample(lower_case,1)
    tempass3 = random.sample(numbers,1)
    tempass4 = random.sample(special,1)
    minreq = tempass+ tempass2+ tempass3 +tempass4

#Other Random Strings
    tpass = random.sample(allposs, passnum)
    passtotal = minreq + tpass
    password = "".join(passtotal)
    print("Generated Password: \n")
    print(password)
    print("\n")

