#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;


<html lang='en'>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <link href="index.css" rel='stylesheet' type='text/css'>
  <title>家を探そう</title>
</head>
<body style="padding-top: 5rem">
  <nav class="navbar navbar-light bg-light fixed-top">
    <!-- タイトル -->
    <a class="navbar-brand" href="http://localhost:2888/cgi-bin/home.py">Home</a>
    <!-- ハンバーガーメニュー -->
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <!-- ナビゲーションメニュー -->
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="http://localhost:2888/cgi-bin/main.py">search</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://localhost:2888/cgi-bin/vieww.py">view</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://localhost:2888/cgi-bin/detail.py">detail</a>
        </li>
      </ul>
    </div>
  </nav>
 
  <div class=m-3>
    <h1>あなたの探したい物件の条件を記入してください</h1>
    %s
    <p>
    </p>
    <form action="main.py" method="post">
      <div class='路線'>
        <p>
          <h3>路線</h3>
          <input type="text" name="tt" />
        </p>
      </div>
      <div class='駅'>
        <p>
          <h3>駅</h3>
          <input type="text" name="ttt" />
        </p>
      </div>
      <h3>部屋</h3>
      <div class='koumoku'>
        <p class='one'>
            <label>
                <input type="checkbox" name="ワンルーム" value="ワンルーム" />
                ワンルーム
            </label>
            <label>
                <input type="checkbox" name="1K" value="1K" />
                1K
            </label>
            <label>
                <input type="checkbox" name="1DK" value="1DK" />
                1DK
            </label>
            <input type="checkbox" name="1LDK" value="1LDK" />
                1LDK
            </label>
        </p>
        <p class='two'>
            <label>
                <input type="checkbox" name="2K" value="2K" />
                2K
            </label>
            <label>
                <input type="checkbox" name="2DK" value="2DK" />
                2DK
            </label>
            <label>
                <input type="checkbox" name="2LDK" value="2LDK" />
                2LDK
            </label>
            <input type="checkbox" name="3K" value="3K" />
                3K
            </label>
        </p>
        <p class='three'>
            <label>
                <input type="checkbox" name="3DK" value="3DK" />
                3DK
            </label>
            <label>
                <input type="checkbox" name="3LDK" value="3LDK" />
                3LDK
            </label>
            <label>
                <input type="checkbox" name="4K" value="4K" />
                4K
            </label>
            <input type="checkbox" name="4DK" value="4DK" />
                4DK
            </label>
        </p>
        <p class='four'>
            <label>
                <input type="checkbox" name="4LDK" value="4LDK" />
                4LDK
            </label>
            <label>
                <input type="checkbox" name="2SLDK" value="2SLDK" />
                2SLDK
            </label>
            <label>
                <input type="checkbox" name="3SLDK" value="3SLDK" />
                3SLDK
            </label>
        </p>
      </div>
      <div class='category'>
        <h3>カテゴリー</h3>
        <p class='one'>
            <label>
                <input type="checkbox" name="賃貸アパート" value="賃貸アパート" />
                賃貸アパート
            </label>
            <label>
                <input type="checkbox" name="賃貸マンション" value="賃貸マンション" />
                賃貸マンション
            </label>
            <label>
                <input type="checkbox" name="賃貸一戸建て" value="賃貸一戸建て" />
                賃貸一戸建て
            </label>
        </p>
      </div>
      <p>
      <h3>築年数</h3>
        <input type="text" name="x" />
      </p>
      <p>
      <h3>駅までのアクセス時間(分・徒歩)</h3>
        <input type="text" name="y" />
      </p>
      <p>
      <h3>何回建か</h3>
        <input type="text" name="z" />
      </p>
      <p>
      <h3>探したい階数</h3>
        <input type="text" name="q" />
      </p>
      <p>
      <h3>家賃(万円)</h3>
        <input type="text" name="g" />
      </p>
      <p>
      <h3>管理費(千円)</h3>
        <input type="text" name="d" />
      </p>
      <p>
      <h3>敷金(万円)</h3>
        <input type="text" name="t" />
      </p>
      <p>
      <h3>礼金(万円)</h3>
        <input type="text" name="w" />
      </p>
      <p>
      <h3>面積(m2)</h3>
        <input type="text" name="b" />
      </p>
      <input type="submit" />
    </form>
  </div>
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>

</body>
</html>
'''

import cgi
from logging.handlers import DEFAULT_TCP_LOGGING_PORT
import os, sys
from pprint import pp
import numpy as np
import pandas as pd
from retry import retry
import requests
from bs4 import BeautifulSoup
from sklearn.metrics.pairwise import cosine_similarity
import webbrowser
from sklearn import preprocessing
#import Levenshtein

try:
    import msvcrt
    msvcrt.setmode(0, os.O_BINARY)
    msvcrt.setmode(1, os.O_BINARY)
except ImportError:
    pass

def is_num(s):
    return s.replace(',', '').replace('.', '').replace('-', '').isnumeric()

f = cgi.FieldStorage()
tt = f.getfirst('tt', '')
ttt = f.getfirst('ttt', '')

lst=[]
if f.getfirst('ワンルーム', ''):
    lst.append('ワンルーム')
if f.getfirst('1K', ''):
    lst.append('1K')
if f.getfirst('1DK', ''):
    lst.append('1DK')
if f.getfirst('1LDK', ''):
    lst.append('1LDK')
if f.getfirst('2K', ''):
    lst.append('2K')
if f.getfirst('2DK', ''):
    lst.append('2DK')
if f.getfirst('2LDK', ''):
    lst.append('2LDK')
if f.getfirst('3K', ''):
    lst.append('3K')
if f.getfirst('3DK', ''):
    lst.append('3DK')
if f.getfirst('3LDK', ''):
    lst.append('3LDK')
if f.getfirst('4K', ''):
    lst.append('4K')
if f.getfirst('4DK', ''):
    lst.append('4DK')
if f.getfirst('4LDK', ''):
    lst.append('4LDK')
if f.getfirst('2SLDK', ''):
    lst.append('2SLDK')
if f.getfirst('3SLDK', ''):
    lst.append('3SLDK')
cate=[]
if f.getfirst('賃貸アパート', ''):
    cate.append('賃貸アパート')
if f.getfirst('賃貸マンション', ''):
    cate.append('賃貸マンション')
if f.getfirst('賃貸一戸建て', ''):
    cate.append('賃貸一戸建て')

# ここから処理の内容を書く。
#スクレイピング
#def parapara():

# スクレイピングするURL
#ここであらかじめスクレイピングするページ(区域)とページ数を指定する(スーモで絞った区間)
#(参照:https://myfrankblog.com/scraping-suumo-website/)
##参照したコードはここから
#base_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&cb=0.0&ct=9999999&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50&page={}"
#konnkai_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=012&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&ek=060007530&rn=0600&pc=50&page={}"
shinagawa = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13109&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&srch_navi=1&pc=70&page={}'
@retry(tries=3, delay=10, backoff=2)
def get_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

all_data = []
#指定した条件(url)での読み込むページ数
max_page = 3

for page in range(1, max_page+1):
    # define url 
    url = shinagawa.format(page)
    
    # get html
    soup = get_html(url)
    
    # extract all items
    items = soup.findAll("div", {"class": "cassetteitem"})
    #print("page", page, "items", len(items))
    
    # process each item
    for item in items:
        stations = item.findAll("div", {"class": "cassetteitem_detail-text"})
        
        # process each station 
        for station in stations:
            # define variable 
            base_data = {}

            # collect base information    
            base_data["名前"] = item.find("div", {"class": "cassetteitem_content-title"}).getText().strip()
            base_data["カテゴリー"] = item.find("div", {"class": "cassetteitem_content-label"}).getText().strip()
            base_data["アドレス"] = item.find("li", {"class": "cassetteitem_detail-col1"}).getText().strip()
            base_data["アクセス"] = station.getText().strip()
            base_data["築年数"] = item.find("li", {"class": "cassetteitem_detail-col3"}).findAll("div")[0].getText().strip()
            base_data["構造"] = item.find("li", {"class": "cassetteitem_detail-col3"}).findAll("div")[1].getText().strip()
            
            # process for each room
            tbodys = item.find("table", {"class": "cassetteitem_other"}).findAll("tbody")
            
            for tbody in tbodys:
                data = base_data.copy()

                data["階数"] = tbody.findAll("td")[2].getText().strip()

                data["家賃"] = tbody.findAll("td")[3].findAll("li")[0].getText().strip()
                data["管理費"] = tbody.findAll("td")[3].findAll("li")[1].getText().strip()

                data["敷金"] = tbody.findAll("td")[4].findAll("li")[0].getText().strip()
                data["礼金"] = tbody.findAll("td")[4].findAll("li")[1].getText().strip()

                data["間取り"] = tbody.findAll("td")[5].findAll("li")[0].getText().strip()
                data["面積"] = tbody.findAll("td")[5].findAll("li")[1].getText().strip()
                
                all_data.append(data)    
#参照したコードはここまで。

#データフレームを作成
#ここから自分で作ったプログラム
dff_n= pd.DataFrame(all_data)
txt = dff_n['アクセス']
line=[]
station =[]
for i in txt:
    p = i.split('/')[0]
    z = i.split(' ')[0]
    t = z.split('/')[-1]
    line.append(p)
    station.append(t)
dff_n['路線']= line
dff_n['駅']= station


if not lst:
  if not tt:
    if not ttt:
      #1
      if not cate:
        dff = dff_n
      #2
      else:
        dff = dff_n[dff_n['カテゴリー'].isin(cate)]
    else:
      dff_p = dff_n[dff_n['駅'].str.contains(ttt)]
      #3
      if not cate:
        dff = dff_p
      #4
      else:
        dff = dff_p[dff_p['カテゴリー'].isin(cate)]
  else:
    dff_p = dff_n[dff_n['路線'].str.contains(tt)]
    if not ttt:
      #5
      if not cate:
        dff = dff_p
      #6
      else:
        dff = dff_p[dff_p['カテゴリー'].isin(cate)]
    else:
      dff = dff_p[dff_p['駅'].str.contains(ttt)]
      #7
      if not cate:
        dff = dff_p
      #8
      else:
        dff = dff_p[dff_p['カテゴリー'].isin(cate)]
else:
  dff_u = dff_n[dff_n['間取り'].isin(lst)]
  if not tt:
    if not ttt:
      #9
      if not cate:
        dff = dff_u
      #10
      else:
        dff = dff_u[dff_u['カテゴリー'].isin(cate)]
    else:
      dff_p = dff_u[dff_u['駅'].str.contains(ttt)]
      #11
      if not cate:
        dff = dff_p
      #12
      else:
        dff = dff_p[dff_p['カテゴリー'].isin(cate)]
  else:
    dff_q = dff_u[dff_u['路線'].str.contains(tt)]
    if not ttt:
      #13
      if not cate:
        dff = dff_q
      #14
      else:
        dff = dff_q[dff_q['カテゴリー'].isin(cate)]
    else:
      dff_p = dff_q[dff_q['駅'].str.contains(ttt)]
      #15
      if not cate:
        dff = dff_p
      #16
      else:
        dff = dff_p[dff_p['カテゴリー'].isin(cate)]


# dff_u = dff_n[dff_n['間取り'].isin(lst)]
# dff_p = dff_u[dff_u['路線'].str.contains(tt)]
# dff = dff_p[dff_p['駅'].str.contains(ttt)]
dff.loc[dff['管理費'] == '-','管理費'] = '0円'
dff.loc[dff['礼金'] == '-','礼金'] = '0万円'
dff.loc[dff['敷金'] == '-','敷金'] = '0万円'
dff.loc[dff['築年数'] == '新築','築年数'] = '築0年'
dfg = dff[~dff["アクセス"].str.contains('車')]
df = dfg[~dfg["アクセス"].str.contains('バス')]


df_int = df[["アクセス","築年数","構造","階数","家賃","管理費","敷金","礼金","面積"]]

#数値を抽出
df_int['築年数'] = df['築年数'].str.extract(r'築(\d*)').fillna(0)
df_int['アクセス'] = df['アクセス'].str.extract(r'歩(\d*)').fillna(0)
df_int['階数'] = df['階数'].str.extract(r'(\d*)階').fillna(0)
df_int['構造'] = df['構造'].str.extract(r'(\d*)階').fillna(0)
df_int['家賃'] = df['家賃'].str.extract(r'(\d.*)万').fillna(0)
df_int['管理費'] = df['管理費'].str.extract(r'(\d*)円').fillna(0)
df_int['家賃'] = df['家賃'].str.extract(r'(\d.*)万').fillna(0)
df_int['敷金'] = df['敷金'].str.extract(r'(\d.*)万').fillna(0)
df_int['礼金'] = df['礼金'].str.extract(r'(\d.*)万').fillna(0)
df_int['面積'] = df['面積'].str.extract(r'(\d.*)m').fillna(0)

x = f.getfirst('x', '')
y = f.getfirst('y', '')
z = f.getfirst('z', '')
q = f.getfirst('q', '')
g = f.getfirst('g', '')
d = f.getfirst('d', '')
t = f.getfirst('t', '')
w = f.getfirst('w', '')
b = f.getfirst('b', '')

if is_num(x) and is_num(y) and is_num(z) and is_num(q) and is_num(g) and is_num(d) and is_num(t) and is_num(w) and is_num(b):
  x=float(x)
  y=float(y)
  z=float(z)
  q=float(q)
  g=float(g)
  d=float(d)
  t=float(t)
  w=float(w)
  b=float(b)
  ll = d*1000

  df_y = pd.DataFrame(
  data=np.array([[y,x,z,q,g,ll,t,w,b]]),
                                columns=['アクセス','築年数','構造','階数','家賃','管理費','敷金','礼金','面積'])
                        

##発表した時に使っていたもの
  # dfq= df_int[["アクセス", "構造"]]
  # dfs= df_y[["アクセス", "構造"]]
  # dq= df_int[["築年数","階数"]]
  # dqq= df_y[["築年数","階数"]]
  # kk= df_int[["面積","管理費"]]
  # kka= df_y[["面積","管理費"]]
  # so= df_int[["家賃","敷金",'礼金']]
  # sos= df_y[["家賃","敷金",'礼金']]
  # math_akusesu = cosine_similarity(dfq,dfs)
  # math_akus = cosine_similarity(dq,dqq)
  # math_as = cosine_similarity(kk,kka)
  # math_s = cosine_similarity(so,sos)

  # df['ruizido1'] = math_akusesu
  # df['ruizido2'] = math_akus
  # df['ruizido3'] = math_as
  # df['ruizido4'] = math_s
  # df['ruizido'] = (df['ruizido1'] + df['ruizido2']+ df['ruizido3']+ df['ruizido4'])/4

  ##正規化を使っての類似度計算
  dfd = pd.concat([df_int,df_y],ignore_index=True)
  dfd['アクセス'] = preprocessing.scale(dfd['アクセス'])
  dfd['築年数'] = preprocessing.scale(dfd['築年数'])
  dfd['構造'] = preprocessing.scale(dfd['構造'])
  dfd['階数'] = preprocessing.scale(dfd['階数'])
  dfd['家賃'] = preprocessing.scale(dfd['家賃'])
  dfd['管理費'] = preprocessing.scale(dfd['管理費'])
  dfd['敷金'] = preprocessing.scale(dfd['敷金'])
  dfd['礼金'] = preprocessing.scale(dfd['礼金'])
  dfd['面積'] = preprocessing.scale(dfd['面積'])

  kurabe = dfd.tail(1)
  moto = dfd.drop(len(dfd) - 1)
  math_akusesu = cosine_similarity(moto,kurabe)
  df['ruizido'] = math_akusesu
  df_c = df.sort_values('ruizido', ascending=False)
  df_y['路線']  = tt
  df_y['駅'] = ttt
  text = '/'.join(lst)
  df_y['間取り'] = text
  textt = '/'.join(cate)
  df_y['カテゴリー'] = textt
  df_y.to_csv('../WebTest_final/cgi-bin/your_data.csv',mode='w')
  df_c.to_csv('../WebTest_final/cgi-bin/metadata_ruizido.csv',mode='w')
  #sum = df_c.to_html()
  url = "http://localhost:2888/cgi-bin/vieww.py"
  webbrowser.open(url,new=0,autoraise=True)



    
else:
  sum='キーワードと数値を入力してください'


print(html % sum)