#establishing connection->request the web page-->retrieve the info---> close the cont

# import socket
# mysoc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysoc.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysoc.send(cmd)

# while True:
#     data = mysoc.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode(),end='')
# mysoc.close()

#urllib usage for handling web page in file format

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# count=dict()
# for line in fhand:
#     word=line.decode().strip()
#     for words in word:
#         count[words]=count.get(words,0)+1
#     print(word)
# print("word count=", count)

#using beautifulsoup
#webpage parsing, returns the connection of the first page to the second page , linkages 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url="http://www.dr-chuck.com/page1.htm"
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))




