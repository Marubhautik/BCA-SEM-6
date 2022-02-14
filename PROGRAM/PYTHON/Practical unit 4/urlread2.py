import urllib.request
def main():
    weburl= urllib.request.urlopen('https://www.youtube.com/user/guru99com')
    print("result code:"+ str(weburl.getcode()))
    data =weburl.read()
    print(data)
if __name__=="__main__":
    main()

"""result code:200
b'<!DOCTYPE html><html style="font-size: 10px;font-family: Roboto, """