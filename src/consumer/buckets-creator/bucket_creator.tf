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
# s3_buckets

resource "aws_s3_bucket" "source-bucket-sdcc-20-21" {
  bucket = "source-bucket-sdcc-20-21"
  acl    = "private"
}

resource "aws_s3_bucket" "message-bucket-sdcc-20-21" {
  bucket = "message-bucket-sdcc-20-21"
  acl    = "private"
}
