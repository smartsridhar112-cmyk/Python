#1.
'''
text="Sridhar"
length=len(text)
print(length)
'''

#2.
'''
text="sridhar"
print(text.upper())
'''

#3.
'''
text="SRIDHAR"
print(text.lower())
'''


'''
text="Sridhar"
r=''
for i in text:
    r=i+r
print(r)
'''

#4.
'''
text="HEllO WORLD"
print(text.startswith("H"))
'''

#5.
'''
text="HELLO WORLD"
print(text.endswith("WORLD"))
'''

#6.
'''
text="HELLO WORLD"
print(text.count('L'))
'''

#7.
'''
a="fake people "
print(a.replace("fake","Don't trust anyone"))
'''

#8.
'''
b="       buffallo"
print(b.lstrip())
'''

#9.
'''
c="P,R,I,Y,A"
name=c.split(",")
#print(name)
'''

#10.
'''
joined="".join(name)
print(joined)
'''

#11.
'''
r="PRIYA"
#print(r[4])
print(r[-5])
'''

#12.
'''
s="WHY ARE I ALIVE IN THIS WORLD"
start=0
end=15
sub=s[start:end]
print(sub)
'''

#13.
'''
c="I am very toxic person"
reverse=c[::-1]
print(reverse)
'''

#14.
'''
s="Hello123"
print(s.isalnum())
'''

#15.

'''
string="this task very tough"
vowels="aeiouAEIOU"
count=0
for len in string:
    if len in vowels:
        count+=1
print(count)
'''

#16.
'''
s="HELLO"
print(s.isalpha())
'''

#17.
'''
p="75845"
print(p.isdigit())
'''

#18.
'''d="sridhar"
print(d.title())
'''

#19.
'''
s="hello world"
print(s.swapcase())
'''

#20.
'''
d="hello World"
substring="world"
index=d.find(substring)
print(index)
'''

