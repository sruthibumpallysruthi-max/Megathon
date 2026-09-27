positive=0
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
print("Zero=",zero)       