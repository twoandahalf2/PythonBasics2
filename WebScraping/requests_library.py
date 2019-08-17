import requests

###GET
# response = requests.get('https://www.devdungeon.com/')
#
# print(response.text) # whole html body
# print(response.status_code) #
# print(response.headers)


###POST
response = requests.post('https://httpbin.org/anything',
                         files={'file': 'The file contents'}, # can pass a list of files
                         data={'form_field_name':'form_value'},
                         params={'q': 5, 'action':'delete'})
###httpbin.org
print(response.text)


##OR stream data in upload

with open('large-file.txt', 'rb') as f:
    response = requests.post('https://httpbin.org/anything', data=f)

print(response.text)