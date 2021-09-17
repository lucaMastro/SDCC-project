terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
   region = "us-east-1"
}

# ----------------------------------------------------------
# s3_buckets_object

resource "aws_s3_bucket_object" "object" {
  bucket = "source-bucket-sdcc-20-21"
  key    = "sources-1.0.zip"
  source = "./sources-1.0.zip"

  #etag = filemd5("./sources-1.0.zip")
}

