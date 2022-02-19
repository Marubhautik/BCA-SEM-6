import requests

response = requests.get("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg")
file = open("sample_imgage.jpg","wb")
file.write(response.content)
file.close()