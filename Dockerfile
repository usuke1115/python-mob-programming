# ベースイメージの指定
FROM python:3.12-slim

# 作業ディレクトリの設定
WORKDIR /web

# DBデータを格納するフォルダ作成
RUN mkdir data

# 一応セキュリティ対策のパッケージバージョンアップ
RUN apt-get update && apt-get install \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# 必要なパッケージのインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# 環境変数ファイルをコピー
COPY .env .

# server.pyを作業ディレクトリ配下へコピー
COPY flask/server.py .

# アプリケーションファイルをコンテナ内の作業ディレクトリにコピー
COPY flask/app/ app/

# アプリケーションの実行
CMD ["python", "server.py", "--host=0.0.0.0"]
