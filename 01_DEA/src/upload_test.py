import boto3
    
s3 = boto3.client('s3')
BUCKET_NAME = "yoshirin-study-bucket-20260315"

def upload_hello():
    print(f" '{BUCKET_NAME}'へでーたを送信します・・・")


    # メモリ上のテキストデータを S3 に直接書き込む
    try:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key="raw/hello-from-python.txt",
            Body="Hello Terraform and Python! This is my first DE Step."
        )
        print("✅　アップロード成功！ 'raw/hello-form-python.txt'が作成されました。")
    except Exception as e:
        print(f"✖　失敗しました: {e}")

if __name__ =="__main__":
    upload_hello()