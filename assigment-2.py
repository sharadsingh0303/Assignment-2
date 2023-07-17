#1.Write a Python program to remove all consecutive duplicates of a given string

'''Input: S = “aabccdba”
Output: abcd'''
s = "aabccdba"

new_s = ''
i = 0
for x in s:
    if s.index(x) == i:
        new_s+=x
    i+=1
print(new_s)

print('---------------------------------------------------------------------------------------------------------------------------')

#2.Write a Python program find the common values that appear in two given strings
s1 = 'Python3'
s2 = 'Python2.7'
result = ''
print('Original strings:')
print(s1)
print(s2)
for ch in s1:
    if ch in s2 and ch not in result:
        result+=ch
print('Intersection of two string said:\n',result)

print('---------------------------------------------------------------------------------------------------------------------------')

#3.Write a Python program to remove unwanted characters from a given string
s1 = 'A%^!B#*CD'
print('original string: ')
print(s1)
result =''

for ch in s1:
    if ch.isalpha():
        result+=ch

print('After removing unwanted characters')
print(result)


print('---------------------------------------------------------------------------------------------------------------------------')

#4.Write a Python program to split a given multiline string in to a list of lines

str = "This is multiline string"
print('Original string:')
print(str)
new_str = str.split()
print('After spliting the string')
print(new_str)

print('---------------------------------------------------------------------------------------------------------------------------')

#5.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
lower = 1500
upper = 2700
new_num = []
for num in range(lower,upper+1):
    if num%7==0 and num%5==0:
        new_num.append(num)

print(new_num)

#return output in string
lower = 1500
upper = 2700
new_num = []
for num in range(lower,upper+1):
    if (num%7==0) and (num%5==0):
        new_num.append(str(num))

print(','.join(new_num))

#using list comprhension
result = [num for num in range(1500,2701) if num%7==0 and num%5==0]
print(result)

#using list comprhension but output return in string
result = ','.join([str(num) for num in range(1500,2701) if num%7==0 and num%5==0])
print(result)

#above same program but a little bit different
result = [str(num) for num in range(1500,2701) if num%7==0 and num%5==0]
print(','.join(result))

#more example
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listtostr = ' '.join([str(elem) for elem in s])

print(listtostr)

print('---------------------------------------------------------------------------------------------------------------------------')

#7.Write a Python program to guess a number between 1 to 9.Note: User is prompted to enter a guess.If the user guesses wrong then the 
# prompt appears again until the guess is correct,on successful guess,user will get a "Wellguessed! "message, and the program will exit
import random

computer_num= random.randint(1,10)
guess_num = 0

while computer_num!=guess_num:
    guess_num= int(input('Guess a number between 1 and 10 until you get it right : '))
print('well guessed')



print('---------------------------------------------------------------------------------------------------------------------------')

#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# ∙Note: Use'continue'statement. 
#∙ExpectedOutput:0 1 2 4 5

for i in range(0,6):
    if i==3 or i==6:
        continue
    print(i,end=' ')

print('---------------------------------------------------------------------------------------------------------------------------')

 #9 questions
'''Write a Python program which iterates the integers from 1 to 50.For multiples of three print "Fizz"
    instead of the number and for the multiples of five print "Buzz".For numbers which are multiples of both three and five print"FizzBuzz".
Sample Output:
∙fizzbuzz
∙1
∙2
∙fizz
∙4
∙Buzz'''

for i in range(0,51):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
        continue
    elif i%3==0:
        print('Fizz')
        continue
    elif i%5==0:
        print('Buzz')
        continue
    print(i)   

print('---------------------------------------------------------------------------------------------------------------------------')

#10.Write a Python program that accepts a string and calculate the number of digits and letters. 
# ∙Sample Data:Python3.2  
# ∙Expected Output: 
# ∙Letters6
# ∙Digits2

sample = 'Python32'
letter = 0
digit = 0
for chr in sample:
    if chr.isalpha():
        letter+=1
    else:
        digit+=1
print(letter)
print(digit)


#same above program using different method
string = 'python32'
alpha = 0
for i in string:
    if i.isalpha():
        alpha+=1

print('number of alphabets is',alpha)
print('number of digit is',len(string)-alpha)


#same program but when we have '.' in string - 'python3.2'.
sample = 'Python3.2'
letter = 0
digit = 0
for chr in sample:
    if chr.isalpha():
        letter+=1
    else:
        digit+=1
print(letter)
print(digit)

#same program 
sample = 'python3.2'
l = 0
d = 0
for i in sample:
    if i.isalpha():
        l+=1
    elif i.isdigit():
        d+=1
    else:
        pass
print(l)
print(d)

#using list comprehensioncmd
sample = 'python3.2'
letters = sum([1 for i in sample if i.isalpha()])
digits = sum([1 for char in string if char.isdigit()])
print(letters)
print(digits)






