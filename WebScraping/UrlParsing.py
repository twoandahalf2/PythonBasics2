from urllib.parse import urlparse, urlunparse

parsed_url = urlparse('https://devdungeon.com/test/node/1?q=5&x=that#test_fragment')

print(parsed_url)
print(parsed_url.scheme)
print(parsed_url.netloc)
print(parsed_url.path)
print(parsed_url.params)
print(parsed_url.query) # use url encoding
print(parsed_url.fragment)


##create URL
new_url = urlunparse(('https','www.devdungeon.com', '/archive', None, 'q=5&x=that', 'test_fragment'))
print(new_url)