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

[http://localhost:5000](http://localhost:5000)にアクセスして「Hello Docker」が表示されるのを確認して下さい。
