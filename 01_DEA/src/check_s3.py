import boto3

s3 = boto3.client('s3')

def run_test():
    print("🚀　AWS　S3　接続テストを開始します・・・")
    try:
        response = s3.list_buckets()
        buckets = [b['Name'] for b in response['Buckets']]

        target = "yoshirin-study-bucket-20260315"
        if target in buckets:
            print(f"✅ 成功:　'{target}'を認識しました！")
        else:
            print(f"！警告:　バケット一覧にはアクセスできましたが、’{target}'が見当たりません。")   

    except Exception as e:
        print(f"✖ エラーが発生しました: {e}")

if __name__=="__main__":
    run_test()