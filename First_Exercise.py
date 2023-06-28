#This prgram is made with the while loop
# number = 3
# while number!=0:
#     print("This number is: ",number)
#     number-=1
# print("Go!!")

#What is it about?
'''Write a program that prompts the user to enter a password. 
Keep prompting until the user enters the correct password, which is "password123". 
Once the correct password is entered, print "Access granted!".
Hey!! But don't go too fast, you only have 3 lifes'''

promptPassword=input('Enter a password: ')
lives=3
while promptPassword!='password123':
    lives-=1
    print("The entered password is invalid, try again")
    promptPassword=input('Enter a password: ')


    if(lives==0):
        break

if lives==0:
    print("Game over")
    
else:
    print("Access granted!")