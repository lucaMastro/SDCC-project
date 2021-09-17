#!/bin/sh

root=`pwd`
buckets_creator_path=$root/buckets-creator
buckets_object_upload_path=$root/src-upload
infrastructure_path=$root/infrastructure 


# delete sources:
cd $buckets_object_upload_path 
terraform destroy

# delete buckets:
cd $buckets_creator_path 
terraform destroy 

# delete infrastucture:
cd $infrastructure_path 
terraform destroy
