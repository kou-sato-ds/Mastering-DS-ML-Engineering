# 1. ベース環境：Python 3.9が入った軽量Linux(slim版)を使用
FROM python:3.9-slim

# 2. 作業ディレクトリ：コンテナ内の実行場所を /app に固定
WORKDIR /app

# 3. ファイルコピー：ローカルの全ファイルをコンテナの /app にコピー
COPY . /app

# 4. ライブラリ構築：キャッシュを保持せず numpy と pandas をインストール
RUN pip install --no-cache-dir numpy pandas

# 5. コンテナ起動時に、名前を変えた step3.py を実行する
CMD ["python", "notebooks/step3.py"]