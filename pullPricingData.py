### /home/vladi/Desktop/LiveCode/EngineeringMan/bitcoinprice.mp4



import sys
import requests


if len(sys.argv) < 2:
    print('please supply some coins to track')
    quit()


coin = sys.argv[1]

template = 'http://api.bittrex.com.api/v1.1/public/getticker?market=btw-{}'
pricing = requests.get(template.format(coin)).json()


print(pricing)