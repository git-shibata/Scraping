from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import pandas as pd
import time

# 今回は30ページ分のデータを取得してみる。
page_num = 30
stock_temp = []
for i in range(page_num):
    # Yahoo Financeのページ。url末尾の数字を変更すると日経225の過去のデータが取得できる。
    url = "http://info.finance.yahoo.co.jp/history/?code=998407.O&sy=2010&sm=12&sd=4&ey=2017&em=3&ed=4&tm=d&p=" + str(i+2)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    # 上記urlのソースをみると<td>~~~</td>にほしい数値が入っているっぽいから、soup.find_all("td")でその部分を抽出する。
    # soup.find_all("td")では<td>~~~</td>といったタグと一緒にリスト型で結果を抽出してくるので、
    # リストのそれぞれの要素に対してget_textメソッドを使って数値だけにする。
    stock_extract = [value.get_text() for value in soup.find_all("td")[3:103]]
    stock_temp.extend(stock_extract)

    time.sleep(0.5)

stock_temp = np.array(stock_temp)


stock = stock_temp.reshape(int(len(stock_temp)/5), 5)
stock = pd.DataFrame(stock[:,1:5], columns=["start", "high", "low", "end"], index=stock[:,0])

# 株価のカラムが文字列になっていて、かつカンマが入っているのでカンマを除去してfloat型にする。
for i in range(4):
    stock.iloc[:,i] = stock.iloc[:,i].str.replace(",", "").astype(float)

print(stock)
