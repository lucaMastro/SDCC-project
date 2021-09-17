#!/bin/sh

root=`pwd`
buckets_creator_path=$root/buckets-creator
buckets_object_upload_path=$root/src-upload
infrastructure_path=$root/infrastructure 

zip -r src-upload/sources-1.0.zip handlers.py

# creating buckets:
cd $buckets_creator_path 
terraform init
terraform apply

# add sources:
cd $buckets_object_upload_path 
terraform init
terraform apply

# creating infrastucture:
cd $infrastructure_path 
terraform init
terraform apply
