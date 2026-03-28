import boto3

def batch_read_s3():
    s3 = boto3.client('s3')
    bucket_name = "yoshirin-study-bucket-20260315"
    prefix = "raw/"

    print(f"--- S3バケット内 ({prefix}) をスキャン中... ---")

    try:
        # 1. ファイル一覧の取得
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        if 'Contents' in response:
            for obj in response['Contents']:
                file_key = obj['Key']
                # フォルダ自体（末尾が /）はスキップ
                if file_key.endswith('/'):
                    continue
                
                print(f"\n[Processing: {file_key}]")

                # --- 昨日の処理をループ内に移植 ---
                res = s3.get_object(Bucket=bucket_name, Key=file_key)
                content = res['Body'].read().decode('utf-8')

                line_count = len(content.splitlines())
                print(f"  ・内容(抜粋): {content[:30]}...")
                print(f"  ・行数: {line_count}")

                if "Python" in content or "Terraform" in content:
                    print("  ✅ バリデーション成功")
                else:
                    print("  ⚠️ キーワードが見つかりません")
        else:
            print("ファイルが見つかりません。")

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    batch_read_s3()