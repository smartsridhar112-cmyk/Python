#.Function

#1.
'''
def find_largest_number(num):
    return max(num)
numbers=[10,203,47,55,77,76]
print(find_largest_number(numbers))
'''

#2.
'''
def count_vowels(a):
    vowels="aeiouAEIOU"
    return sum(1 for len in a if len in vowels)
string="My name is Sridhar"
print("vowel count:",count_vowels(string))
'''

#3.
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter your number:"))
print("Factoial of",num,"is:",factorial(num))
'''

#4.
'''
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input("Enter your number"))
print(num,"is prime",is_prime(num))
'''                   
        
#5.

'''
def reverse_string(s):
    reversed_s=""
    for char in s:
        reversed_s=char+reversed_s
    return reversed_s
string=input("Enter your :")
print("reversed string:",reverse_string(string))
'''

#6.
'''
def remove_duplicate(s):
    return list(set(s))
numbers=[1,2,1,4,2,5,3,7,7,7,4,5,1,5,3,5,4,5,8,5]
print(remove_duplicate(numbers))
'''

#7.
'''
def simple_interest(p,r,t):
    return (p*r*t)/100
principal=int(input("Enter your principal :"))
rate=int(input("Enter your rate :"))
time=float(input("Enter your Time Period :"))
print("simple Interest :",simple_interest(principal,rate,time))
'''

#8.
'''
def is_palindrome(s):
    return s==s[::-1]
p=input("Enter :")
print(p, "is plaindrome :", is_palindrome(p))
'''

#9.
'''
def fibonacci_series(n):
    fib=[0,1]
    while len(fib)<n:
        fib.append(fib[-1]+fib[-2])
    return fib[:n]
n=int(input("Enter number :"))
print(fibonacci_series(n))
'''

#10.

#11.
'''
def count_word(word):
    return len(word)           
word=input("enter your sentence :")
print("Your word count is : ",count_word(word))
'''

#12.



#13.
'''
def celsius_to_Fahreneit(c):
    return (c*9/5)+32
c=float(input("Enter your Celsius :"))
print("your celsius value is :",c,"and your Fahreneit is :",celsius_to_Fahreneit(c))
'''

#14.
'''
def sum_of_digit():
    num=int(input("Enter your digit :"))
    sum=0
    while num>0:
        sum+=num%10
        num//=10
    print(sum)
sum_of_digit()
'''

#15.
'''
def even_number():
    num=int(input("Enter your number :"))
    if num%2==0:
        print("it is",num,"even number")
    else :
        print("it is odd number")
even_number()
'''
