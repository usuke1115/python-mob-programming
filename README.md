**セットアップ手順**

**手順1: Dockerを起動する**

Docker Desktopを開いて、Dockerが正常に起動していることを確認します。

**手順2: Dockerfileがあるディレクトリに移動**

ターミナルまたはコマンドプロンプトを開き、このプロジェクトのDockerfileが存在するディレクトリに移動します。

**手順3: envファイルをコピー**

ターミナルまたはエクスプローラーにて、example.envをコピーして.envを作成する

```sh
$ cp example.env .env
```

**手順4: Dockerイメージをビルド**

次のコマンドを実行して、Dockerイメージをビルドします。  
`docker compose build`  
これにより、python-mob-programming-appという名前のイメージがバージョンv1.0としてビルドされます。

**手順5: アプリケーションを実行する**

ビルドしたDockerイメージからコンテナを起動し、アプリケーションを実行します。  
`docker compose up`  
これにより、アプリケーションが起動できます！  

[http://localhost](http://localhost)にアクセスして「Hello Docker」が表示されるのを確認して下さい。


**開発者向け**

パッケージマネージャーに[poetry](https://cocoatomo.github.io/poetry-ja/basic-usage/)を使用しています。

***開発時初期設定***

```sh
$ poetry install
```

上記コマンドでvenvが作成され、パッケージのインストールが完了します。

***testの実行***

```sh
$ docker compose -f docker-compose.yaml -f docker-compose.override.test.yaml run --rm flask 
```

上記コマンドで
