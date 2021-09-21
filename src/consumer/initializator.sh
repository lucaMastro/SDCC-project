#!/bin/sh

root=`pwd`
buckets_creator_path=$root/buckets-creator
buckets_object_upload_path=$root/src-upload
infrastructure_path=$root/infrastructure 
db_path=$root/db 

zip -r src-upload/sources-1.0.zip handlers.py

# creating buckets:
cd $buckets_creator_path 
terraform init
echo 'yes' | terraform apply

# add sources:
cd $buckets_object_upload_path 
terraform init
echo 'yes' | terraform apply

# creating infrastucture:
cd $infrastructure_path 
terraform init
echo 'yes' | terraform apply

# creating db:
cd $db_path
terraform init
echo 'yes' | terraform apply

# db initialization 
mysql -h `aws rds describe-db-instances --filters "Name=engine,Values=mysql" \
  --query "*[].[Endpoint.Address]"  --output text` -P 3306 -u admin \
  --password='sdcc-db-admin' < $db_path/db_generation.sql

