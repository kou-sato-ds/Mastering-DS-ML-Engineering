import boto3
from botocore.exceptions import NoCredentialsError
import config

def upload_to_s3():
    # S3クライアントの初期化
    s3 = boto3.client('s3')

    try:
        print(f"Uploading {config.LOCAL_FILE_PATH} to s3://{config.S3_BUCKET_NAME}/{config.S3_OBJECT_KEY}...")
        
        # ファイルのアップロード実行
        s3.upload_file(config.LOCAL_FILE_PATH, config.S3_BUCKET_NAME, config.S3_OBJECT_KEY)
        
        print("Upload Successful!")
        
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available (AWS CLIの設定を確認してください)")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    upload_to_s3()