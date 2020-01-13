from urllib.request import Request, urlopen

url = "https://i4.mangapanda.com/naruto/1/naruto-1564778.jpg"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

file_name = url.split('/')[-1]
u = urlopen(req)

f = open(file_name, 'wb')

while True:
    buffer = u.read()
    if not buffer:
        break
    f.write(buffer)

f.close()