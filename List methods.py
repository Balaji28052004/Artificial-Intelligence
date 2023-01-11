string=input("Enter elements:")
a=string.split()
print("The List is :",a)
a[0]=1
print(a)
a.append(7)
print(a)
a.extend([5,6,7])
print(a)
del a[5]
print(a)
