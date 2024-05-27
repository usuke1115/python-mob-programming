# pythonパッケージのビルド
FROM python:3.12-slim as build

# 作業ディレクトリの設定
WORKDIR /web

# 一応セキュリティ対策のパッケージバージョンアップ
RUN apt-get update && apt-get install -y curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# poetryのインストール
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"


# poetry関連ファイルのコピー
COPY pyproject.toml .
COPY poetry.lock .
 
# パッケージインストール
RUN poetry config virtualenvs.create false && \
  poetry install && \
  rm -rf ~/.cache


# 実行環境
FROM python:3.12-slim as prod

# 作業ディレクトリの設定
WORKDIR /web

ENV PYTHONPATH=/web

# DBデータを格納するフォルダ作成
RUN mkdir data

# 一応セキュリティ対策のパッケージバージョンアップ
RUN apt-get update && apt-get install \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# 必要なパッケージのインストール
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# 環境変数ファイルをコピー
COPY .env .

# server.pyを作業ディレクトリ配下へコピー
COPY flask/server.py .

# アプリケーションファイルをコンテナ内の作業ディレクトリにコピー
COPY flask/app/ app/

# アプリケーションの実行
CMD ["python", "server.py", "--host=0.0.0.0"]
