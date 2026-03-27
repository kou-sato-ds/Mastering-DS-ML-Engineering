import boto3

def read_s3_content():
    # 1. S3クライアントの初期化
    s3 = boto3.client('s3')
    
    # 2. ターゲットとなるバケット名とファイルパス（キー）を指定
    # ※ご自身のバケット名に書き換えてください
    bucket_name = "yoshirin-study-bucket-20260315" 
    file_key = "raw/hello-from-python.txt"

    print(f"--- S3からデータを取得中: s3://{bucket_name}/{file_key} ---")

    try:
        # 3. get_objectでファイルを取得
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        
        # 4. 内容を読み取り（StreamingBodyをデコード）
        content = response['Body'].read().decode('utf-8')
        
        print("\n[取得したデータの内容]")
        print("-" * 30)
        print(content)
        print("-" * 30)

        # 5. 簡易バリデーション（データエンジニアの嗜み）
        line_count = len(content.splitlines())
        word_count = len(content.split())
        
        print(f"\n[データ解析結果]")
        print(f"・行数: {line_count}")
        print(f"・単語数: {word_count}")
        
        if "Python" in content:
            print("✅ チェック完了: 期待されるキーワード 'Python' が含まれています。")
        else:
            print("⚠️ 警告: キーワードが見つかりません。")

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    read_s3_content()