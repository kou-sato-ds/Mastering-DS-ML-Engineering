import boto3

# S3 クライアントの作成
s3 = boto3.client('s3')
def check_my_bucket(target_name):
    # バケット一覧を取得
    response = s3.list_buckets()

    print("---既存のバスケット一覧---")
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    for name in buckets:
        print(f" - {name}")


    if target_name in buckets:
        print(f"\n✅　成功:バケット　'{target_name}' を検出しました！")
    else:
        print(f"\n✖　失敗: バケット  '{target_name}' が見つかりません。 Terraform applyを確認してください。")

if __name__=="__main__":
    MY_BUCKET = "yoshirin-study-bucket-20260315"
    check_my_bucket(MY_BUCKET)