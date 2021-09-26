#!/bin/sh

root=`pwd`
buckets_path=$root/buckets-creator
infrastructure_path=$root/infrastructure 
db_path=$root/db 
src_path=$root/python_source

# delete sources:
cd $src_path 
echo 'yes' | terraform destroy

# delete buckets:
cd $buckets_path
aws s3 rm s3://message-bucket-sdcc-20-21 --recursive
echo 'yes' | terraform destroy 

# delete infrastucture:
cd $infrastructure_path 
echo 'yes' | terraform destroy

# delete database
cd $db_path 
echo 'yes' | terraform destroy
