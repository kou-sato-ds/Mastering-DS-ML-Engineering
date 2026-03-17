provider "aws" {
  region = "ap-northeast-1"
}

resource "aws_s3_bucket" "my_study_bucket" {
  # 直接名前を書くのではなく、変数から呼び出す
  bucket = var.bucket_name

  tags = {
    Name        = "MyStudyBucket"
    Environment = "Dev"
  }
}