provider "aws" {
  region = "us-east-1"
}

# data "aws_availability_zones" "available" {}

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
