import requests
#print version of request
print(requests.__version__)

#get Google homepage
response = requests.get('http://www.google.com/')
#print (response.status_code)

r = requests.get('https://raw.githubusercontent.com/zoeypu98/C404Lab/main/lab1.py')
print(r.text)
