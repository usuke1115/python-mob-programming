#このファイルとフォルダのように「Flaskプロジェクト」の
#「フォルダ名」と「ファイル名」は異なってもいい

from flask import Flask, render_template ,redirect
#2つ目はhtmlテンプレートを差し込むためのモジュール
#3つ目はリダイレクトをできるようにするためのモジュール

flsk = Flask(__name__)

#この下のflskはFlaskオブジェクトのインスタンス
@flsk.route("/")#URL「/」が呼ばれたときの関数
def index():
            
    ct = "<h1>目次</h1>"
    ct += "<a href = '/chap1'>第一章</a>"
    ct += "<p><a href='/chap2'>第二章</a></p>"
    return ct

@flsk.route("/chap1")
def chap1():
    ct = "<h1>第一章</h1>"

    titles = ['一、丸底','二、平底','三、三角','四、メス']

    for i,v in enumerate(titles):
        # enumerateは (0,'一、丸底')、(1,'二、平底')、(2,'三、三角')、(3,'四、メス')みたいに
        # インデックスとvalueを連想配列のようにしたようなオブジェクトを返す
        # =の右のfは変数を文字列に埋め込むときに使う
        ct += f"<p><a href='/chap1/{i+1}'>{v}フラスコ</a></p>"

    return ct

@flsk.route("/chap1/<section>")
#上のchap1関数でURLの<section>の部分に入力された文字列を関数の引数として用いることができる
#ただし、整数として用いるのであればintを用いてデータ型を整数型に変換
def sections(section):

    #文字列のリストを用意しておく
    cts = ['全体が丸く、転がりやすいが熱に強い',
            '底だけが平たく、置きやすいが熱に弱い',
            '底に行くほど広いので反応効率が良い',
            '首の印のメニスカスを合わせて体積を一定にできる。フタ必須']

    ct = "準備中" #最初にこれを与えておく
    try:
        section_num = int(section)-1 #※リストのインデックスは０開始
        if section_num in range(4):#0～3の間に入るか判定
            ct = cts[section_num] #ctxをインデックスで取り出す
    except: #（URLに）例外処理、条件式で評価できない値（ここでは整数値以外が入った場合）
        ct=('掲載予定はありません')

    return f"<p>{ct}</p><a href='/chap1'>第一章</a>"

materials = [('glass','ガラス'),
            ('plastic','プラスチック'),
            ('flouric','フッ素樹脂'),
            ('stainless','ステンレス')]

@flsk.route("/chap2")
def chap2():
    return render_template("chap2.html",materials = materials)
        #render_templateでテンプレートとしてhtmlを読み込む
        #第二引数はLaravelでいうcompact関数のようなものと思われる
        #キーワード＝渡す値

#<a href="/chap2/{{ material[0]}}">{{material[1]}}</a>とchap2.htmlに記述していることに注意

@flsk.route("/chap2/<material>")
#URLに適切な材料名を入力した場合、その説明文を出力する
def show_material(material):
    for item in materials:
        if material == item[0]:
            return render_template(f"{material}.html",material_name = item[1])
    
    #render_templateはLarvelでいうところのview関数に強い
    #該当しなければ、第二章のページにリダイレクト
    return redirect("/chap2")