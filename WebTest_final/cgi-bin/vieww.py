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
    <h1>閲覧</h1>
    <p>
      <h2>今回選んだ条件</h2>
      <table class="table table-bordered">
      %s
      </table>
    </p>
    <p>
      <h2>上記の条件で探した結果</h2>
      %s
    </p>
  </div>
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>
'''

import cgi
import os, sys
import numpy as np
import pandas as pd
from retry import retry
import requests
from bs4 import BeautifulSoup
from sklearn.metrics.pairwise import cosine_similarity
#import Levenshtein

try:
    import msvcrt
    msvcrt.setmode(0, os.O_BINARY)
    msvcrt.setmode(1, os.O_BINARY)
except ImportError:
    pass


content=''
table_rgb=''
table_face = ''
df = ''
img = ''
endtxt = ''
files=[]
U = ''
form = cgi.FieldStorage()



df_0 = pd.read_csv('../WebTest_final/cgi-bin/your_data.csv')
df = df_0.drop(['Unnamed: 0'],axis=1)
table_you = df.to_html(escape=False)


dff_0 = pd.read_csv('../WebTest_final/cgi-bin/metadata_ruizido.csv')
dff = dff_0.drop(['Unnamed: 0','路線','駅','ruizido'],axis=1)
table_ruizido = dff.to_html(escape=False)


print(html % (table_you,table_ruizido))


