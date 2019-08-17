## HTTP GET and POST requests with standard library

from urllib.request import urlopen, Request


##open url with string
response = urlopen('https://www.cars.bg')
print(response.read())

print(20 * '=')

#prebuild the request
request = Request('https://www.cars.bg')
request.add_header('User-Agent', 'Not Firefox')
response = urlopen(request)
print(response.read())

