import requests


url = 'https://www.facebook.com/favicon.ico'
r = requests.get(url, allow_redirects=True)

open('facebook.ico', 'wb').write(r.content)

#Test Deployy
