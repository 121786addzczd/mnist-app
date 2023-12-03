## asdfで使用するpythonの依存関係にあるものをインストールする
**Mac OS**
```shell
brew install readline sqlite3 xz zlib tcl-tk
```

## asdfで使用するpythonプラグインをインストール
```shell
asdf plugin add python
```

mnist-appディレクトリを作成し移動
```shell
mkdir mnist-app && cd mnist-app
```

mnist-app配下に.tool-versionsファイル作成しpython 3.9.13と書き込む
```shell
echo "python 3.9.13" > .tool-versions
```

.tool-versionsで指定したpythonをインストールする
```shell
asdf install
```

pythonがインストールされたか確認する
```shell
python --version
```

asdfのプラグインの一覧を表示
```shell
asdf plugin-list-all
```

poetryを含む行を検索する
```shell
asdf plugin-list-all | grep poetry
```

poetryのプラグインを追加する
```shell
asdf plugin-add poetry
```

.tool-versionsファイルにpoetry 1.1.14を記載
```shell
echo "poetry 1.1.14" >> .tool-versions
```

.tool-versionsで指定した、poetryを導入
```shell
asdf install
```

poetryがインストールされたか確認
```shell
poetry --version
```

trainディレクトリ作成し、移動
```shell
mkdir train && cd train
```


```shell
poetry init
```
いくつか質問されるが全てエンターでOK
trainディレクトリ配下にpyproject.tomlファイルが作成されます。
これはpoetryでinstallするライブラリを管理するファイルになります。
このファイルにインストールするライブラリのバージョンや名前を書いておけば、このファイルを共有することでいつでも同じライブラリ、バージョンをインストールできる。


asdfのpythonのパスを取得します
```shell
which python
```
コマンド実行後、/Users/user名/.asdf/shims/pythonといった形で表示されます。

which pythonで見つかったpythonをpoetryで使用するよう設定
```shell
poetry env use /Users/user名/.asdf/shims/python
```
※user名は表示されるユーザーによって変わります

poetryで使用するpythonバージョンがpyprojectに指定したバージョンが表示されるか確認
```shell
poetry run python --version
```

poetryの仮想環境一覧を表示する
```shell
poetry env list
```


scikit-learnインストール
```shell
poetry add scikit-learn@1.1.2
```

pythonの実行
```shell
poetry run python <実行したいpythonファイル名>
```

scikit-learnの学習結果をONNX形式で保存するためのライブラリインストール
```shell
poetry add skl2onnx@1.15
```

packagingライブラリインストール
```shell
poetry add packaging@21.3
```

画像処理でよく使用するライブラリを導入
```shell
poetry add Pillow@9.2.0
```

ONNX Runtimeで推論するために必要なライブラリを導入
```shell
poetry add onnxruntime
```


### FastAPIの準備

FastAPIのディレクトリ作成
```shell
mkdir python-web-app
```

fastapiのディレクトリ移動
```
cd python-web-app
```

python-web-appディレクトリ内で以下コマンド実行（全てEnter）
```
poetry init
```
pyproject.tomlが作成されます

使用するpythonのパスを指定(which pythonで見れる)
```shell
poetry env use /Users/<ユーザー名>/.asdf/shims/python
```

pyproject.tomlのpythonバージョンになっているか確認
```shell
poetry run python --version
```

