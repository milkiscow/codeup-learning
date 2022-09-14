#1
print("Hello")

#2
print("Hello World")

#3
print("Hello\nWorld")

#4
print("'Hello'")

#5
print('"Hello World"')

#6
print("\"!@#$%^&*()\'")

#7
print("\"C:\Download\\'hello'.py\"")

#8
print("print(\"Hello\\nWorld\")")

#9
a = input()
b = input()
print(b)
print(a)

#10
f = float(input())
for i in range(3):
    print(f)
    
#11
a,b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)

#12
y,m,d = input().split('.')
print(d+'-'+m+'-'+y)

#13
a,b = input().split('-')
print(a+b)

#14
h,m,s = input().split(':')
print(m)

#15
f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
print(f1**f2)

#16
f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
print(format(f1/f2, ".3f"))

#17
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f"))

#18
a, b = input().split()
a = int(a)
b = int(b)
if a == False and b == False:
    print(True)
else:
    print(False)
    
#19