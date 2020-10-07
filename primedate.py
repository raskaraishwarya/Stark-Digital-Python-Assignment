import requests, json 

api_key = "API KEY"

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=API KEY&q"

date = eval(input("Enter date:"))

url = base_url + "appid=" + api_key + "&q=" + date

response = requests.get(url) 

n = response.json()

def isPrime(n):
    if(n<2):
        return False
    for i in range(2,n//2+1):
        if(n%i == 0):
            return False
    return True

if isPrime(date):
    print(date,"is Prime Date")
else:
    print(date,"is Not Prime Date")
