import boto3

def upload_samples():
    s3 = boto3.client('s3')
    bucket_name = "yoshirin-study-bucket-20260315"
    
    # アップロードするファイルの内容（3パターン）
    samples = {
        "raw/test_python.txt": "Hello from Python! Learning DEA is fun.",
        "raw/test_terraform.txt": "Infrastructure as Code with Terraform is powerful.",
        "raw/test_other.txt": "Just a normal text file without keywords."
    }

    print(f"--- S3 ({bucket_name}) へテストデータを一括アップロード中 ---")

    for key, content in samples.items():
        try:
            s3.put_object(Bucket=bucket_name, Key=key, Body=content)
            print(f"✅ 成功: {key}")
        except Exception as e:
            print(f"❌ 失敗: {key} ({e})")

if __name__ == "__main__":
    upload_samples()