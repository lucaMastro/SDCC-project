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
# sqs-queue

resource "aws_sqs_queue" "send_messages_sqs_queue" {
  name = "send_messages_sqs_queue"
  message_retention_seconds = 86400  
}

# ----------------------------------------------------------
# roles

resource "aws_iam_role" "registration_login_iam_role" {
  name = "registration_login_iam_role"

  assume_role_policy = jsonencode(
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
)
}

resource "aws_iam_role" "usr_list_iam_role" {
  name = "usr_list_iam_role"

  assume_role_policy = jsonencode(
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
)
}

resource "aws_iam_role" "read_message_iam_role" {
  name = "read_message_iam_role"

  assume_role_policy = jsonencode(
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
)
}

resource "aws_iam_role" "send_message_iam_role" {
  name = "send_message_iam_role"

  assume_role_policy = jsonencode(
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole", 
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
)
}


resource "aws_iam_role" "manage_del_and_mark" {
  name = "manage_del_and_mark"

  assume_role_policy = jsonencode(
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
)
}
# ----------------------------------------------------------
# policies


resource "aws_iam_policy" "sqs_policy" {
  name        = "sqs_policy"
  path        = "/"
  description = "IAM policy for a lambda"

  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "sqs:SendMessage",
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:GetQueueAttributes",
        "sqs:ChangeMessageVisibility"
      ],
      "Resource": "arn:aws:sqs:us-east-1:*:*",
      "Effect": "Allow"
    }
  ]
})
}


resource "aws_iam_policy" "s3_write_policy" {
  name        = "s3_write_policy"
  path        = "/"
  description = "IAM policy for a lambda"

  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
            "Effect": "Allow",
            "Action": [
              "s3:PutObject",
              "s3:PutObjectTagging", #this permits to tag objects
            ],
            "Resource": [
              "arn:aws:s3:::message-bucket-sdcc-20-21",
              "arn:aws:s3:::message-bucket-sdcc-20-21/*"
            ]
    }
  ]
})
}


resource "aws_iam_policy" "s3_read_policy" {
  name        = "s3_read_policy"
  path        = "/"
  description = "IAM policy for a lambda"

  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
            "Effect": "Allow",
            "Action": [
              "s3:ListBucket",
              "s3:GetObject",
              "s3:GetObjectTagging", #this permits to read tag
            ],
            "Resource": [
              "arn:aws:s3:::message-bucket-sdcc-20-21",
              "arn:aws:s3:::message-bucket-sdcc-20-21/*"
            ]
    }
  ]
})
}

resource "aws_iam_policy" "s3_delete_policy" {
  name        = "s3_delete_policy"
  path        = "/"
  description = "IAM policy for a lambda"

  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
            "Effect": "Allow",
            "Action": [
              "s3:ListBucket",
              "s3:DeleteObject",
            ],
            "Resource": [
              "arn:aws:s3:::message-bucket-sdcc-20-21",
              "arn:aws:s3:::message-bucket-sdcc-20-21/*"
            ]
    }
  ]
})
}

resource "aws_iam_policy" "lambda_logging" {
  name        = "lambda_logging"
  path        = "/"
  description = "IAM policy for logging from a lambda"

  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    }
  ]
})
}


resource "aws_iam_policy" "lambda_rds" {
  name        = "lambda_rds"
  path        = "/"

  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
          "rds:DescribeDBInstances",
      ],
      "Resource": "arn:aws:rds:*:*:*"
      "Effect": "Allow"
    }
  ]
})
}
# ----------------------------------------------------------
# policy attachment


# reg_log 

resource "aws_iam_role_policy_attachment" "reg_log_policy_log_attach" {
  role = aws_iam_role.registration_login_iam_role.name
  policy_arn = aws_iam_policy.lambda_logging.arn
}

resource "aws_iam_role_policy_attachment" "reg_log_policy_attach_s3_write" {
  role = aws_iam_role.registration_login_iam_role.name
  policy_arn = aws_iam_policy.s3_write_policy.arn
}

resource "aws_iam_role_policy_attachment" "reg_log_policy_attach_rds" {
  role = aws_iam_role.registration_login_iam_role.name
  policy_arn = aws_iam_policy.lambda_rds.arn
}

# usr_list
resource "aws_iam_role_policy_attachment" "usr_list_policy_log_attach" {
  role       = aws_iam_role.usr_list_iam_role.name
  policy_arn = aws_iam_policy.lambda_logging.arn
}


# read_message 

resource "aws_iam_role_policy_attachment" "read_message_policy_attach_s3_read" {
  role       = aws_iam_role.read_message_iam_role.name
  policy_arn = aws_iam_policy.s3_read_policy.arn
}
resource "aws_iam_role_policy_attachment" "read_message_policy_log_attach" {
  role       = aws_iam_role.read_message_iam_role.name
  policy_arn = aws_iam_policy.lambda_logging.arn
}


# send_message 

resource "aws_iam_role_policy_attachment" "send_message_policy_attach_sqs" {
  role       = aws_iam_role.send_message_iam_role.name
  policy_arn = aws_iam_policy.sqs_policy.arn
}

resource "aws_iam_role_policy_attachment" "send_message_policy_attach_s3_write" {
  role       = aws_iam_role.send_message_iam_role.name
  policy_arn = aws_iam_policy.s3_write_policy.arn
}
resource "aws_iam_role_policy_attachment" "send_message_policy_attach_s3_read" {
  role       = aws_iam_role.send_message_iam_role.name
  policy_arn = aws_iam_policy.s3_read_policy.arn
}

resource "aws_iam_role_policy_attachment" "send_message_policy_log_attach" {
  role       = aws_iam_role.send_message_iam_role.name
  policy_arn = aws_iam_policy.lambda_logging.arn
}


# manage_del_and_mark

resource "aws_iam_role_policy_attachment" "manage_del_and_mark_log_attach" {
  role       = aws_iam_role.manage_del_and_mark.name
  policy_arn = aws_iam_policy.lambda_logging.arn
}
resource "aws_iam_role_policy_attachment" "manage_del_and_mark_s3_write" {
  role       = aws_iam_role.manage_del_and_mark.name
  policy_arn = aws_iam_policy.s3_write_policy.arn
}
resource "aws_iam_role_policy_attachment" "manage_del_and_mark_s3_read" {
  role       = aws_iam_role.manage_del_and_mark.name
  policy_arn = aws_iam_policy.s3_read_policy.arn
}
resource "aws_iam_role_policy_attachment" "manage_del_and_mark_policy_attach_s3_delete" {
  role       = aws_iam_role.manage_del_and_mark.name
  policy_arn = aws_iam_policy.s3_delete_policy.arn
}
# ----------------------------------------------------------
# Lambda functions

resource "aws_lambda_function" "sign_log_in" {
   function_name = "sign_log_in"

   s3_bucket = "source-bucket-sdcc-20-21"
   s3_key    = "sources.zip"

   handler = "lambda_reg_log.sign_in_log_in"
   runtime = "python3.8"

   role = aws_iam_role.registration_login_iam_role.arn
   depends_on = [
      aws_s3_bucket.source-bucket-sdcc-20-21,
      aws_s3_bucket_object.object,
   ]
}

resource "aws_lambda_function" "users_list" {
   function_name = "users_list"

   s3_bucket = "source-bucket-sdcc-20-21"
   s3_key    = "sources.zip"

   handler = "lambda_users_list.users_list"
   runtime = "python3.8"

   role = aws_iam_role.usr_list_iam_role.arn
   depends_on = [
      aws_s3_bucket.source-bucket-sdcc-20-21,
      aws_s3_bucket_object.object,
   ]
}


resource "aws_lambda_function" "read_messages" {
   function_name = "read_messages"

   s3_bucket = "source-bucket-sdcc-20-21"
   s3_key    = "sources.zip"

   handler = "lambda_read.read_messages"
   runtime = "python3.8"

   role = aws_iam_role.read_message_iam_role.arn
  
   depends_on = [
      aws_s3_bucket.source-bucket-sdcc-20-21,
      aws_s3_bucket_object.object,
   ]
}

resource "aws_lambda_function" "send_message" {
   function_name = "send_message"

   s3_bucket = "source-bucket-sdcc-20-21"
   s3_key    = "sources.zip"

   handler = "lambda_send.send_message"
   runtime = "python3.8"

   role = aws_iam_role.send_message_iam_role.arn
   depends_on = [
      aws_s3_bucket.source-bucket-sdcc-20-21,
      aws_s3_bucket_object.object,
   ]
}


resource "aws_lambda_function" "manage_del_and_mark" {
   function_name = "manage_del_and_mark"

   s3_bucket = "source-bucket-sdcc-20-21"
   s3_key    = "sources.zip"

   handler = "delete_and_mark.manage_del_and_mark"
   runtime = "python3.8"

   role = aws_iam_role.manage_del_and_mark.arn
   depends_on = [
      aws_s3_bucket.source-bucket-sdcc-20-21,
      aws_s3_bucket_object.object,
   ]
}


#----------------------------------------------------------
# map for send_message input

resource "aws_lambda_event_source_mapping" "read_messages_source_map" {
  event_source_arn = aws_sqs_queue.send_messages_sqs_queue.arn
  function_name    = aws_lambda_function.send_message.arn
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

# ----------------------------------------------------------
# s3_buckets_object

resource "aws_s3_bucket_object" "object" {
  bucket = "source-bucket-sdcc-20-21"
  key    = "sources.zip"
  source = "./sources.zip"

  #etag = filemd5("./sources.zip")
  depends_on=[
      aws_s3_bucket.source-bucket-sdcc-20-21,
  ]
  
}

# ----------------------------------------------------------
# rds_istance

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "2.77.0"

  name                 = "sdcc"
  cidr                 = "10.0.0.0/16"
  azs                  = ["us-east-1a","us-east-1b"]
  public_subnets       = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
  enable_dns_hostnames = true
  enable_dns_support   = true
}

resource "aws_db_subnet_group" "sdcc-subnet" {
  name       = "sdcc-subnet"
  subnet_ids = module.vpc.public_subnets

}

resource "aws_security_group" "sdcc-rds-security-group" {
  name   = "sdcc-rds-security-group"
  vpc_id = module.vpc.vpc_id

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

}

resource "aws_db_parameter_group" "rds-parameter-group" {
  name   = "rds-parameter-group"
  family = "mysql5.7"

}

resource "aws_db_instance" "sdcc-rds" {
  identifier             = "sdcc-rds"
  instance_class         = "db.t2.small"
  allocated_storage      = 10
  engine                 = "mysql"
  engine_version         = "5.7"
  username               = "admin"
  password               = "sdcc-db-admin"
  db_subnet_group_name   = aws_db_subnet_group.sdcc-subnet.name
  vpc_security_group_ids = [aws_security_group.sdcc-rds-security-group.id]
  parameter_group_name   = aws_db_parameter_group.rds-parameter-group.name
  publicly_accessible    = true
  skip_final_snapshot    = true
}
