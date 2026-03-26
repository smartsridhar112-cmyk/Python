#.1
'''
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if num1>=num2 and num1>=num3:
    print("the largest number is first number:",num1)
elif num2>=num1 and num2>=num3:
    print("the largest number is second number:",num2)
else :
    print("the largest number is third number :",num3)
'''

#.2
'''
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if num1<=num2 and num1<=num3:
    print("the smallest number is first number:",num1)
elif num2<=num1 and num2<=num3:
    print("the smallest number is second number:",num2)
else :
    print("the smallest number is third number :",num3)
'''

#.3
'''
num=int(input("Enter your number"))
if num>0:
    print("Positive",num)
elif num<0:
    print("negative",num)
else:
    print("Zero")
'''

#.4
'''
num=int(input("Enter the number"))
if num%5==0:
    print("it's multiple of 5",num)
elif num%3==0:
    print("it's multiple of 3",num)
elif num%7==0:
    print("it's multiple of 7",num)
else:
    print30("not multiple of 3,5,7")

'''



#.5
'''
days=int(input("Enter number of late days:"))

if days<=5:
    fine=days*0.40
elif days<=10:
    fine=((days)*0.65)
else :
    fine=((days)*0.80)
print("late days",days)
print("total fine Rs.",fine)
'''


#.6
'''
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

op=input("Enter the operation(+,-.*,/):")

if op=="+":
    print("Result:",num1+num2)
elif op=="-":
    print("Result:",num1-num2)
elif op=="*":
    print("Result:",num1*num2)
elif op=="/":
    print("Result:",num1/num2)
else :
    print("Error:Divison by Zero")
    
'''

#.7
'''
weight=int(input("Enter the weight of parcel in grams:"))
booking=input("Enter booking type: Ordinary/Express :")

if booking=="Ordinary":
    if weight<100:
        charge=80
    elif weight<500:
        charge=150
    elif weight<1000:
        charge=210
    else :
        charge=250

elif booking=="Express":
    if weight<100:
        charge=100
    elif weight<500:
        charge=200
    elif weight<1000:
        charge=250
    else :
        charge=300

else :
    charge=None
    print("Invaild booking type")

if charge is not None:
    print("Parcel Weight:",weight,"gm")
    print("Booking type:",booking)
    print("charge:₹",charge)
'''

#.8
'''
price=int(input("Enter the price of Laptop:"))

if price<50000:
    discount=0
elif price<=100000:
    discount=price*0.10
elif price<150000:
    discount=price*0.15
else :
    discount=price*0.20

total_price=price-discount

print("Price of Laptop:",price)
print("Discount",discount)
print("Total Price:",total_price)
'''

        
