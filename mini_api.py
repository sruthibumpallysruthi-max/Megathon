import requests
try:
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code==200:
        data=response.json()
        for user in data:
            print("Name:",user["name"])
            print("Email:",user["email"])
    else:
        print("failed to fetch data")
except requests.RequestException:
    print("Somehting went wrong while connecting to api")                