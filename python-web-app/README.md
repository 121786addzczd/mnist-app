# 手書き数字推論アプリケーション

FastAPIのディレクトリ作成
```shell
mkdir python-web-app
```

fastapiのディレクトリ移動
```shell
cd python-web-app
```

python-web-appディレクトリ内で以下コマンド実行（全てEnter）

```shell
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
