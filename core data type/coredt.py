'''
#.LIST


#1.
s=["Lion","Monkey","Tiger","Elephant","Gorizla"]

#2.
#print(s[1])
#print(s[-1])

#3.
sublist=s[1:3]
#print(sublist)

#4.
s.append("FOX")
#print(s)

#5.
s.insert(3,"jaguar")
#print(s)

#6.
s.extend(["Dog","cat"])
#print(s)

#7.
s.remove("Monkey")
#print(s)

#8.
s.pop()
del s[2]
#print(s)

#9.
s.index("Lion")
#print(s)

#10.
count=s.count("Lion")
#print(s)

#11.
s.sort()
#print(s)

#12.
s.reverse()
#print(s)
'''


#TUPLE

#1.
'''
a=(10,20,30,40,50)
print(a)
'''
#2.
'''
a=(10,20,30,40,50)
print(a[2])
print(a[-3])
'''
#3.
'''
a=(10,20,30,40,50)
print(a[1:4])
'''

#4.
'''
number=(10,20,30,10,40,10,20)
print(number.count(10))
'''

#5.
'''
a=(10,20,30,40,50)
print(a.index(40))
'''
#6.
'''
t1=(11,22,33)
t2=(44,55,66)
concantenate=t1+t2
print(concantenate)
'''

#7.
'''
a=(70,80,90)
repeat=a*3
print(repeat)
'''

#8.
'''
a=(10,20,30,40)
b=list(a)
print(b)
'''

#9.
'''
a=(10,20,30,40,50,60,70,80,90,100)
b=len(a)
print(b)
'''

#10.
'''
t=(10,20,30)
print(20 in t)
'''

#12.
'''
numbers=(1,2,3,4,5)
total=0
for num in numbers:
    total+=num
print(total)
'''


#SET

#1.
'''
num={10,20,30,40,50}
#print(num)

#2.
num={10,20,30,40,50}
num.add(60)
print(num)


#3.
num={10,20,30,40,50}
num.remove(10)
print(num)
'''

#4.
'''
num={10,20,30,40,50}
num.clear()
print(num)
'''

#5.
'''
a={10,20,30}
b={10,30,50}
union=a.union(b)
print(union)
'''

#6
'''
a={70,77,80,27}
b={68,77,84,27}
inter_section=a.intersection(b)
print(inter_section)
'''

#7.
'''
a={10,20,30,40}
b={10,30,50,70}
different=a.difference(b)
print(different)
'''

#8.
'''
a={11,22,33,44}
b={44,33,66,77}
symmetric_difference=a.symmetric_difference(b)
print(symmetric_difference)
'''

#9.
'''
a={10,20}
b={10,20,30}
subset=a.issubset(b)
print(subset)
'''

#10.
'''
a={90,80,70,60}
b={70,60}
superset=a.issuperset(b)
print(superset)
'''

#11.
'''
a={77,66,55}
print(a.copy())
'''

#12.
'''
total=0
num={1,2,3,4,5,6,7,8,9}
for n in num:
    total+=n
print(total)
'''

#Dictonary

#1.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
print(Student_Details)
'''

#2.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
print(Student_Details["Favourite_place"])
'''

#3.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
print(Student_Details.values())

'''
#4.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
Student_Details.update({"Favourite_Movie":"Pirates of the caribbeen"})
print(Student_Details)
'''

#5.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
removed_value=Student_Details.pop("Age")
print("Rmeoved Value:",removed_value)
print(Student_Details)
'''

#6.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
print(Student_Details.popitem())
'''

#7.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
print(Student_Details.keys())
'''

#8.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
print(Student_Details.values())
'''

#9.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
print(Student_Details.items())
'''

#10.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
print("City" in Student_Details)
'''

#11.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
print("keys:")
for key in Student_Details.keys():
    print(key)

print("values:")
for value in Student_Details.values():
    print(value)

print("item:")
for item in Student_Details.items():
    print(item)
'''

#12.
'''
Student_Details={
    "Name":"Sridhar",
    "Age":21,
    "City":"Salem",
    "Favourite_Color":"Sky_Blue",
    "Favourite_place":"Finland"
    }
copy=Student_Details.copy()
print("copy File:",copy)
'''
