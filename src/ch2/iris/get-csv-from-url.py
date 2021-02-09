# https://note.nkmk.me/python-download-web-images/
import os
import pprint
import time
import urllib.error
import urllib.request
import pandas as pd

#pattern 1
def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:

        print(e)

url = "https://raw.githubusercontent.com/kujirahand/book-mlearn-gyomu/master/src/ch2/iris/iris.csv"
#decide directory path and downloded file name
dst_path = './iris-url.csv'
download_file(url, dst_path)

#pattern 1-symple
'''
https://docs.python.org/ja/3/reference/compound_stmts.html#the-with-statement

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file, open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())
    except urllib.error.URLError as e:
        print(e)
'''

# pattern 2 not recommended
# https://github.com/kujirahand/book-mlearn-gyomu/blob/master/src/ch2/iris/iris.csv
# download file
"""
url = "https://raw.githubusercontent.com" + \
      "/kujirahand/book-mlearn-gyomu/master/src/ch2/iris" + \
      "/iris.csv"
savefile = "iris-url.csv"
urllib.request.urlretrieve(url, savefile)
print("Saving files is succeeded")

csv = pd.read_csv(savefile, encoding="utf-8")
csv
"""
