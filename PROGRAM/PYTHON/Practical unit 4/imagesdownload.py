import os
import requests
from bs4 import *


def Create_Dir(images):
    try:
        dir_name = input("Enter Dir name :")
        if dir_name == "":
            dir_name = "Downloads"
        else:
            os.mkdir(dir_name)
    except:
        print("Directory already exist :")
        Create_Dir()

    ContentDownload(images, dir_name)


def ContentDownload(images, dir_name):
    count = 0
    print(f"Total {len(images)} files found to download")

    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                link = image["data-srcset"]
            except:
                try:
                    link = image["data-src"]
                except:
                    try:
                        link = image["data-fallback-scr"]
                    except:
                        try:
                            link = image["src"]
                        except:
                            pass

            try:
                r = requests.get(link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:

                    with open(f"{dir_name}/image{i + 1}.jpg", "wb") as f:
                        f.write(r)
                    count += 1
            except:
                pass

            # if count == len(images):
            #     print("All images downloaded")
            # else:
            #     print(f"")


def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img')
    Create_Dir(images)


url = input("Enter url :")
main(url)


'''Enter url :https://hardikchavda.in/
Enter Dir name :bhautik
Total 9 files found to download'''