#!/bin/sh

root=`pwd`
buckets_creator_path=$root/buckets-creator
buckets_object_upload_path=$root/src-upload
infrastructure_path=$root/infrastructure 
db_path=$root/db 

# delete sources:
cd $buckets_object_upload_path 
echo 'yes' | terraform destroy

# delete buckets:
cd $buckets_creator_path 
echo 'yes' | terraform destroy 

# delete infrastucture:
cd $infrastructure_path 
echo 'yes' | terraform destroy

# delete database
cd $db_path 
echo 'yes' | terraform destroy
