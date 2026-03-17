# 変数の定義
variable "bucket_name" {
  description = "The name of the S3 bucket"
  # "string" ではなく string （クォーテーションを消す）にする
  type        = string
  default     = "yoshirin-study-bucket-20260315"
}