# ベースイメージの指定
FROM python:3.12-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# wsgi.pyを作業ディレクトリ配下へコピー
COPY wsgi.py .

# アプリケーションファイルをコンテナ内の作業ディレクトリにコピー
COPY flaskr/ flaskr/

# アプリケーションファイルをコンテナ内の作業ディレクトリにコピー
COPY data/ data/

# アプリケーションの実行
CMD ["flask", "run", "--host=0.0.0.0"]
