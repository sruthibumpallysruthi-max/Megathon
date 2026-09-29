'''for i in range(6):
    print(i)

for i in range(1,9):
    print(i)    

for i in range(0,11,2):
    print(i)

for i in range(1,11):
    if i%2==0:
        print(i)'''

#while,continue and break
'''i=1
while i<=5:
    print(i)
    i+=1        

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,18):
    if i==7:
        continue
    print(i)'''

'''for i in range(1,6):
    for j in range(1,6):
        print(i,j)'''

'''for i in range(1,6):
    for j in range(i): #or range(1,i+1)
        print("*",end="")
    print()

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")  
    print()      

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print() '''

'''for i in range(1,21):
    if i%3==0:
        print(i)

for i in range(1,11):
    if i%2==0:
        print(i,"Even number")
    else:
        print(i,"odd number")'''

'''sum=0
for i in range(1,11):
    print(i)
    sum+=i
print(sum)'''

'''sum=0
for i in range(1,21):
    if i%2==0:
     print(i)
     sum+=i
print(sum) '''

'''largest=0
for i in range(5):
 n=int(input("Enter a number:"))
 if n>largest:
  largest=n
print("Largest=",largest)'''  

'''smallest=None
for i in range(5):
 n=int(input("Enter a number:"))
 if smallest is None or n<smallest:
  smallest=n
print("Smallest=",smallest)'''

'''largest=None
smallest=None
sum=0
for i in range(5):
    n=int(input("Enter a umber:"))
    if largest is None or n>largest:
        largest=n
    if smallest is None or n<smallest:
        smallest=n
    sum+=n
print("Largest=",largest)
print("Smallest=",smallest)
print("Sum=",sum)'''

'''positive=0
negative=0
zero=0
for i in range(5):
    n=int(input("Enter a number:"))
    if n>0:
        positive+=1
    elif n<0:
        negative+=1
    else:
        zero+=1
print("Positive=",positive)
print("Negative=",negative) 
print("Zero=",zero)'''

'''sum=0
for i in range(5):
    n=int(input("Enter a numer:"))
    sum+=n
    average=sum/5
print("AVerage=",average)'''

'''n=int(input("Enter a number:"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("Factorial=",factorial) '''

'''n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i) '''

'''sum=0
largest=None
smallest=None
even=0
odd=0
for i in range(5):
    n=int(input("Enter a number:"))
    if largest is None or n>largest:
        largest=n
    if smallest is None or n<smallest:
        smallest=n
    if n%2==0:
        even+=1
    else:
        odd+=1    
    sum+=n
    average=sum/5
print("Largest=",largest)
print("Smallest=",smallest)
print("Sum=",sum)
print("Average=",average)
print("Even=",even)
print("Odd",odd)'''



                
 











