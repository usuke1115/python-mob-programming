# ベースイメージの指定
FROM python:3.12-slim

# 作業ディレクトリの設定
WORKDIR /web

# 必要なパッケージのインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# 環境変数ファイルをコピー
COPY .env .

# wsgi.pyを作業ディレクトリ配下へコピー
COPY wsgi.py .

# アプリケーションファイルをコンテナ内の作業ディレクトリにコピー
COPY app/ app/

# アプリケーションファイルをコンテナ内の作業ディレクトリにコピー
COPY data/ data/

# アプリケーションの実行
CMD ["flask", "run", "--host=0.0.0.0", "--debugger", "--reload"]
