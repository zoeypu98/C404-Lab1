import requests
#print version of request
print(requests.__version__)

#get Google homepage
response = requests.get('http://www.google.com/')
print (response.status_code)
print (response.content)
