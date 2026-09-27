'''count=0
text=input("Enter a string:")
for char in text:
    if char in "aeiou":
        count+=1
print("Count=",count)'''        

'''count=0
text=input("Enter a string:")
for char in text:
        if char.isalpha() and char not in "aeiou":
            count+=1
print("Count=",count)'''    

'''count=0
text=input("Enter a string:")
for char in text:
    if char.isdigit():
        count+=1
print("Count=",count)'''

'''count=0
text=input("Enetr a string:")
for char in text:
    if char==" ":
        count+=1
print("Count=",count)'''

'''count = 0
text = input("Enter a string: ")
target = input("Enter a character: ")
for char in text:
    if char == target:
        count += 1
print("Count =", count)'''

'''text=input("Enter a string:")
reverse=text[::-1]
print("Reverse=",reverse)'''


'''text=input("Enter a string:")
reverse=text[::-1]
if text==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")''' 

'''text=input("Enter a sentence :")
words=text.split()
count=len(words)
print("Number of words=",count)'''

'''text="Python Programming"
print(text.startswith("Python"))
print(text.endswith("Programming"))'''

'''text=input("Enter a string:")
print(text.startswith("Python"))
print(text.endswith("ing"))'''

text=input("Enter a sentence")
words=text.split()
word_count=len(words)
vowel_count=0
for char in text:
    if char.lower() in "aeiou":
        vowel_count+=1
digit_count=0
for char in text:
    if char.isdigit():
        digit_count+=1
reverse=text[::-1]
print("Number of words =", word_count)
print("Number of vowels =", vowel_count)
print("Number of digits =", digit_count)
print("Reversed sentence =", reverse)




