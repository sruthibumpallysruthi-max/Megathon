'''largest = None
second = None

numbers = list(map(int, input("Enter numbers: ").split()))

for n in numbers:

    if largest is None:
        largest = n

    elif n > largest:
        second = largest
        largest = n

    elif second is None or n > second:
        if n != largest:
            second = n

print("Largest =", largest)
print("Second largest =", second)'''


'''numbers=list(map(int,input("Enter numbers:").split()))
frequency={}
for n in numbers:
    if n in frequency:
       frequency[n]=frequency[n]+1
    else:
        frequency[n]=1
for number,count in frequency.items():
    print(number,"->",count)'''


'''most_frequent=None
highest_count=None
numbers=list(map(int,input("Enter numbers:").split()))
frequency={}
for n in numbers:
    if n in frequency:
        frequency[n]=frequency[n]+1
    else:
        frequency[n]=1
for number,count in frequency.items():
    if highest_count is None or count>highest_count:
        most_frequent=number
        highest_count=count
print("Most frequent=",most_frequent)
print("Frequency=",highest_count) '''

'''largest = None
smallest = None
most_frequent = None
highest_count = None

numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for n in numbers:

    if largest is None:
        largest = n
    elif n > largest:
        largest = n

    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n


for n in numbers:

    if n in frequency:
        frequency[n] = frequency[n] + 1
    else:
        frequency[n] = 1


for number, count in frequency.items():

    if highest_count is None or count > highest_count:
        most_frequent = number
        highest_count = count


print("Largest =", largest)
print("Smallest =", smallest)
print("Most Frequent =", most_frequent)
print("Highest Count =", highest_count)'''

'''users=[
    {
        "name":"shruthi","age":19,"branch":"csd"
    },
    {
        "name":"aksh","age":18,"branch":"csm"
    }
]    
new_user={
        "name":"akhi","age":19,"branch":"cse"
    }
users.append(new_user)
    
for user in users:
    print(user["name"],user["age"],user["branch"])'''


'''#creating dictionary using list
users=[
    {
        "name":"shruthi","age":19,"branch":"csd"
    },
    {
        "name":"aksh","age":18,"branch":"csm"
    }
]   
#taking input from user 
name=input("Enter name:")
age=int(input("Enter age:"))
branch=input("Enter branch:")
#appending new user
new_user={
        "name":name,"age":age,"branch":branch
    }
users.append(new_user)
#displaying
for user in users:
    print(user["name"],user["age"],user["branch"])'''

#searching name
'''users=[
    {
        "name":"shruthi","age":19,"branch":"csd"
    },
    {
        "name":"aksh","age":18,"branch":"csm"
    }
]    
search_name=input("Enter name to search:")
for user in users:
    if user["name"]==search_name:
        print("user found:")
        print("NAme:",user["name"])
        print("Age:",user["age"])
        print("Branch:",user["branch"])'''

#user not found
'''users=[
    {
        "name":"shruthi","age":19,"branch":"csd"
    },
    {
        "name":"vasu","age":19,"branch":"cse"
    }
]
search_name=input("Enter name to search:")
found=False
for user in users:
    if user["name"]==search_name:
        print("User found:")
        print("Name:",user["name"])
        print("AGe:",user["age"])
        print("Branch:",user["branch"])
        found=True
if found==False:        
    print("User not found")'''

#Error handling
'''age=int(input("Enter age:"))
try:
    age=int(input("Enter age:"))
except ValueError:
    print("Please enter a valid age")'''   

#json
'''import json
users=[
    {"name": "shruthi", "age": 19, "branch": "csd"},
    {"name": "vasu", "age": 19, "branch": "cse"}
]
json_data=json.dumps(users) 
#print(json_data)

python_data=json.loads(json_data)
print(python_data)'''

#api
import json
import requests
users=[
    {
        "name":"shruthi","age":19,"branch":"csd"
    },
    {
        "name":"vasu","age":19,"branch":"cse"
    }
]
json_data=json.dumps(users)
print(json_data)
try:
    #response=requests.get("https://jsonplaceholder.typicode.com/users")
    response = requests.get("https://invalid-url-example-12345.com")
    print(response.status_code)
    if response.status_code==200:
        data=response.json()
        for user in data:
            print("Name:",user["name"])
            print("City",user["address"]["city"])
    else:
       print("Failed to fetch data")
except requests.RequestException:
    print("Something went wrong while connecting to API")
             








    

