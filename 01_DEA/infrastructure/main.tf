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

# 2026-03-24: Terraform Initialized and Plan confirmed. Ready for apply.