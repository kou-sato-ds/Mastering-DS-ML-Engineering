# 1. Glue カタログデータベース（テーブルを格納する箱）
resource "aws_glue_catalog_database" "my_db" {
  name = "yoshirin_study_db"
}

# 2. IAM ロール（クローラがAWSリソースを操作するための権限）
resource "aws_iam_role" "glue_role" {
  name = "AWSGlueServiceRole-S3Scanner"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "glue.amazonaws.com"
      }
    }]
  })
}

# 3. IAM ポリシーのアタッチ（S3の読み取り権限とCloudWatchへのログ出力権限を追加）
resource "aws_iam_role_policy_attachment" "glue_service" {
  role       = aws_iam_role.glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}

# S3バケットへのアクセス権限を個別に追加
resource "aws_iam_role_policy" "glue_s3_access" {
  name = "GlueS3Access"
  role = aws_iam_role.glue_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ]
      Effect   = "Allow"
      Resource = [
        "${aws_s3_bucket.my_study_bucket.arn}",
        "${aws_s3_bucket.my_study_bucket.arn}/*"
      ]
    }]
  })
}

# 4. クローラ本体の設定
resource "aws_glue_crawler" "my_crawler" {
  database_name = aws_glue_catalog_database.my_db.name
  name          = "yoshirin-s3-crawler"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    # 混在を避けるため、CSV専用のフォルダを指定
    path = "s3://${aws_s3_bucket.my_study_bucket.bucket}/csv_data/"
  }
}