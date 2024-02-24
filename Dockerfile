# ベースイメージの指定
FROM python:3.12-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# TODO:SQLiteをインストール

# プロジェクトの全てのファイルをコンテナ内の作業ディレクトリにコピー
COPY . .

# アプリケーションの実行
CMD ["flask", "run", "--host=0.0.0.0"]
