import urllib.request

weburl= urllib.request.urlopen('https://www.youtube.com/c/flutterdev')

print("result code:"+ str(weburl.getcode()))

'''200'''