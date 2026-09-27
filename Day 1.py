'''name="shruthi"
age=19
college="hitam"
branch="csd"
hackathon_team_name="pixel verse"
print(name)
print(age)
print(college)
print(branch)
print(hackathon_team_name)'''

'''score=75
if score>=90:
    print("excellent")
elif score>=60:
    print("good")
else:
    print("average") '''       


'''for i in range(5):
    print(i)'''

'''issues=["water leak","broken light",'garbage'] 
for issue in issues:
    print(issue)'''

'''issues=["water leak","broken light",'garbage'] 
issues.append("patholes") 
issues.remove("garbage")'''

'''student={"name":"shruthi","age":19,"branch":"csd"}
print(student["name"])
print(student["branch"])
student["age"]=20
student["college"]="abc college"'''

'''students=[
    {
        "name":"shruthi",
        "age":19
    },
    {
        "name":"akshitha",
        "age":18
    },
    {
        "name":"vasu",
        "age":19
    }
]
for student in students:
    print(student["name"])'''

'''def greet(name):
    print("Hello",name)
greet("shruthi")  '''   

'''def add(a,b):
    return a+b
result=add(10,20)
print(result)'''

'''students=[
    {
        "name":"shruthi",
        "age":19,
        "branch":"csd"
    },
    {
        "name":"akshitha",
        "age":18,
        "branch":"cse"
    },
    {
        "name":"vasu",
        "age":19,
        "branch":"csm"
    }
]
add_student={"name":"abhi","age":17,"branch":"csm"}
students.append(add_student)
def display_students():
    for student in students:
        print("Name:",student["name"])
        print("Age:",student["age"])
        print("Branch:",student["branch"])
display_students()
def add_student():
    student={
        "name":input("Enter name:"),
        "age":int(input("EEnter age:")),
        "branch":input("Enter branch:")   }
    students.append(student)
add_student()    
display_students()'''

students=[
    {
        "name":"shruthi",
        "age":19,
        "branch":"csd"
    },
    {
        "name":"akshitha",
        "age":18,
        "branch":"cse"
    },
    {
        "name":"vasu",
        "age":19,
        "branch":"csm"
    }
]
add_student={"name":"abhi","age":17,"branch":"csm"}
students.append(add_student)
def display_students():
    for student in students:
        print("Name:",student["name"])
        print("Age:",student["age"])
        print("Branch:",student["branch"])

def add_student():
    student={
        "name":input("Enter name:"),
        "age":int(input("EEnter age:")),
        "branch":input("Enter branch:")   }
    students.append(student)

while True:
    choice=input("Enter your choice: ")
    if choice=="1":
        add_student()
    elif choice=="2":
        display_students()
    elif choice=="3":
        break
    else:
        print("Invalid choice")



