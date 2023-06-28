# This program is made with the for loopnumber = ''
# for number in range(99,2,-3):
#     print("This nuber is: ",number)
# print("Go!")

'''Exercise 2: Sum of Numbers
Write a program that calculates the sum of all numbers from 1 to a given number n. 
Prompt the user to enter the value of n and display the result.'''

userNumber=int(input('Enter a number: '))
totalSum=0
for number in range(1,userNumber,1):
    print('The number is: ',number)
    totalSum+=number
print('The sum is: ',totalSum)