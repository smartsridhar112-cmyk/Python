#if else

#1.
'''
num1=int(input("Enter the first Number"))
num2=int(input("Enter the Second Number"))
smallest= num1 if num1<num2 else num2
print("The smallest Number is :",smallest)
'''

#2.
'''
num1=int(input("Enter the first Number"))
num2=int(input("Enter the Second Number"))
largest= num1 if num1>num2 else num2
print("The largest Number is :",largest)
'''

#3.
'''
num=int(input("Enter your Number"))
absoulte_value=num if num>=0 else -num
print("The absoulte value is :",absoulte_value)
'''

#4.
'''
num=int(input("Enter the number"))
if num%2==0:
    print("it's even number",num)
else:
    print("it's odd number")
'''

#5.
'''
num=int(input("Enter the number"))
if num*5==0:
    print("it's multiple of 5")
else :
    print("it's not multiple of 5")
'''

#6.
'''
num=int(input("Enter the number"))
if num%10==0:
    print("it's multiple of 10")
else :
    print("it's not multiple of 10")
'''

#7.
'''
num=int(input("Enter the Number"))
if 10<= num <=99:
    print("it's two digit number",num)
else :
    print("it's not two digit")

'''

#8.
'''
num=int(input("Enter the number"))
if 100<= num <=999:
    print("it's three digit number",num)
else:
    print("it's not three digit number")
'''

#9.
'''
num=int(input("Enter the number"))
if num%10==0:
    print("the last number is zero",num)
else:
    print("the last number is not zero")
'''

#10.
'''
num=int(input("Enter the number"))
square=num**2
if square>=50:
    print("it's 50 above",square)
else:
    print("it's 50 below")
'''

#11.
'''
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
defferent=num1-num2
if defferent==0:
    print("it's zero",defferent)
else:
    print("it's not zero")

'''

#12.
'''
mark=int(input("Enter your mark"))
if mark>=50:
    print("Pass",mark)
else :
    print("Fail")
'''

#13.
'''
num=int(input("Enter the number"))
if num%10==0:
    print("it's divisable",num)
else:
    print("it's not divisable")
'''
#14.
'''
num=int(input("Enter the number"))
digit1= num %10
digit2= num//10
if digit1<=digit2:
    print("biggest 1")
else:
    print("biggest 2")
'''

#15.
'''
choise=int(input("Enter the number"))
if choise==1:
    print("Exam will be easy")
else :
    print("Exam will be difficult")
'''

#16.
'''
enter=int(input("Enter the number"))
if enter==1:
    print("you can go out and play")
else:
    print("you can not go out and play")
'''

#17.
'''
length=int(input("Enter your length"))
breadth=int(input("Enter your breadth"))
if length==breadth:
    print("it's square")
else :
    print("it's rectangle")
'''

#18.
'''
num=int(input("Enter the number"))
if 65<=num<=90:
    print("ASCII value of Uppercase Alphabet",num)
else:
    print("in this value is not ASCII uppercase Alphabet")
'''

#19.
'''
num=int(input("Enter the number"))
if 97<=num<=122:
    print("ASCII value of lowercase Alphabet",num)
else:
    print("in this value is not ASCII Lowercase Alphabet")
'''

#20.
'''
num=int(input("Enter the number"))
if 48<=num<=57:
    print("ASCII value of Numeric Character",num)
else:
    print("in this value is not ASCII Numeric Character")
'''

#21.
'''
num=int(input("Enter the number"))
if num%5==0 and num%3==0:
    print("both multiple of 5 and 3",num)
else:
    print("not multiple of 3 and 5")
'''

#22.
'''
num=int(input("Enter the number"))
if 100<=num <=999 and num%10==0:
    print("Three digit number multiple of 10:",num)
else :
    print("not three digit number multiple of 10")
'''


#23.
'''
num=int(input("Enter the number"))
if 100<=num <=999 and num%10==0 and num%5==0 and num%2==0: 
    print("Three digit number multiple of 10, 2 and 5:",num)
else :
    print("not three digit number multiple of 10, 2 and 5")
'''

#24.
'''
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
a=num1*num2
b=num1+num2
if num1%2==0 and num2%2==0:
    print("both are even the product is:",a)
else:
    print("bot not even the product of",b)
'''

#25.
'''
num=int(input("Enter the number"))
if num%7==0 :
    print("it is buzz number:",num)
else :
    print("it is not buzz number")
'''

