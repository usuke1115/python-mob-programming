**セットアップ手順**

**手順1: Dockerを起動する**

Docker Desktopを開いて、Dockerが正常に起動していることを確認します。

**手順2: Dockerfileがあるディレクトリに移動**

ターミナルまたはコマンドプロンプトを開き、このプロジェクトのDockerfileが存在するディレクトリに移動します。

**手順3: Dockerイメージをビルド**

次のコマンドを実行して、Dockerイメージをビルドします。  
`docker build -t python-mob-programming-app:v1.0 .`  
これにより、python-mob-programming-appという名前のイメージがバージョンv1.0としてビルドされます。

**手順4: アプリケーションを実行する**

ビルドしたDockerイメージからコンテナを起動し、アプリケーションを実行します。  
`docker run -p 5000:5000 --env-file=./.env -v .:/web python-mob-programming-app:v1.0 `  
これにより、アプリケーションが起動できます！  

[http://localhost:5000](http://localhost:5000)にアクセスして「Hello Docker」が表示されるのを確認して下さい。