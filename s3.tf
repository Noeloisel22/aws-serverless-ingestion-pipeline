resource "aws_s3_bucket" "data_ingestion" {
  bucket = "nloisel-2026-data-pipeline" # Doit être unique au MONDE
}