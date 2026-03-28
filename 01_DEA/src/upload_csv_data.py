import boto3

def upload_csv():
    s3 = boto3.client('s3')
    bucket_name = "yoshirin-study-bucket-20260315"
    
    # CSV形式のデータ
    csv_content = """id,topic,status
1,S3 Foundation,Completed
2,Boto3 Scripting,Completed
3,Glue Crawler,In Progress
4,Athena Query,Pending
5,Data Lake Pipeline,Success"""

    print(f"--- S3 へ CSV データをアップロード中 ---")
    
    try:
        s3.put_object(
            Bucket=bucket_name, 
            Key="csv_data/learning_logs.csv", 
            Body=csv_content,
            ContentType='text/csv'
        )
        print("✅ 成功: csv_data/learning_logs.csv")
    except Exception as e:
        print(f"❌ 失敗: {e}")

if __name__ == "__main__":
    upload_csv()