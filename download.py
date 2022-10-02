import urllib.request
import os

if not os.path.exists("./papka"): os.mkdir("./papka")


url = "https://oval.cisecurity.org/repository/download/5.11.2/vulnerability/microsoft_windows_8.xml"
print(url.split("/")[-1])
#url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
urllib.request.urlretrieve(url, f'./papka/{url.split("/")[-1]}')
