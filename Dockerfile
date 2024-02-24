# ベースイメージの指定
FROM python:3.12-slim

# 作業ディレクトリの設定
WORKDIR /app

# ファイルをコピー
COPY . /app

# 必要なパッケージのインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# データベースファイルを格納するディレクトリの作成
RUN mkdir -p /app/data

# /app/data ディレクトリに対して読み書き実行権限を付与
RUN chmod 777 /app/data

# プロジェクトの全てのファイルをコンテナ内の作業ディレクトリにコピー
COPY . .

# コピーしたファイルに対しても権限を設定
RUN chmod -R 777 /app

# アプリケーションの実行
CMD ["flask", "run", "--host=0.0.0.0"]
