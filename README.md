# Home_search

このプロダクトは、自分が探したい物件を類似度計量を用いて、数値が高い順にユーザに表示する、CGIと類似度計量を用いたwebサイト構築の条件下で作ったものである。

物件探しのwebサイト(スーモ)に実際に載っている物件情報をスクレイピングし、持ってきたデータを元にユーザが選んだ物件の条件に近しい物件を表示させるという機能が主な機能となっている。

スクレイピング機能に関しては、(参照:https://myfrankblog.com/scraping-suumo-website/)こちらのwebページのコードを参照した。

実際に取り出すデータはmain.pyの269行目で指定されており、ここは自分で調べたい区域に絞った状態のスーモのサイトのurlを貼り付ける必要がある。

大まかな、このwebアプリケーションの流れをphotoファイルに画像として保存してある。

### 動かすための必須作業

Mac

・それぞれのpythonファイルの一番上は自分のpythonの環境ごとに変更が必要。<br>
・ターミナル上で<br>
  which python<br>
  と打って出たパスまたは、<br>
  #!/usr/bin/env python<br>
  をpythonファイルの一番上のコードと置き換える。

・ターミナルを開いて、cd WebTest_finalを入力
・その状態で、<br>
  chmod 755 ./cgi-bin/main.py<br>
  chmod 755 ./cgi-bin/home.py<br>
  chmod 755 ./cgi-bin/vieww.py<br>
  chmod 755 ./cgi-bin/detail.py<br>
  をターミナルで入力(それぞれのpythonファイルを読み込む)
  
・上記の四つを入力したら、<br>
  python -m http.server --cgi 2888<br>
  でファイルを実際に動かす(ポート番号は2888で固定させる)　→ 他のファイルへの接続ができなくなっているため
  
・ウェブブラウザ上で、<br>
  http://localhost:2888/cgi-bin/home.py<br>
  を入力することで本webアプリケーションを使用することができる。
