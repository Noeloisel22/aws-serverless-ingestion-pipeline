resource "aws_s3_bucket" "data_ingestion" {
  bucket = var.bucket_name
}