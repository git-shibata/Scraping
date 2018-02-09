# request.urlretriveを使ったScraping
import urllib.request

currency_pair = 'usdjpy'
#currency_pair = 'eurjpy'
#currency_pair = 'gbpjpy'
#currency_pair = 'audjpy'
#currency_pair = 'cadjpy'
#currency_pair = 'chfjpy'
#currency_pair = 'nzdjpy'
#currency_pair = 'sekjpy'
#currency_pair = 'nokjpy'

#スタート日付
start_day     = "20010101"
#終了日を今日に指定
url           = "https://stooq.com/q/d/l/?s=" + currency_pair + \
                "&d1=" + start_day + "&d2=" + dt.today().strftime("%Y%m%d") + "&i=d"
file_name     = currency_pair + '_d.csv'
#取得して、ファイルに保存(よくよく考えると保存しなくてもいいな)
urllib.request.urlretrieve(url, file_name)
