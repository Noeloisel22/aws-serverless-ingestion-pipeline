output "name_output" {
    description = "get name of the bucket"
    value = aws_s3_bucket.data_ingestion.id
}
output "arn_output" {
    description = "get arn of the bucket"
    value = aws_s3_bucket.data_ingestion.arn
}