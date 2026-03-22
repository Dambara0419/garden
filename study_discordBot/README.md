### 仮想環境の作成と立ち上げ
```
bash
uv venv -p 3.12
source .venv/bin/activate
```

deactivateする場合は以下のコマンドを実行してください。
```
bash
deactivate
```

### 依存関係のインストール
```
bash
uv pip install requests pandas
（または　pip install -r requirements.txt）
```

### アプリケーションの起動
```
bash
uv run main.py
(もしくは　uv run python example.py)

```
