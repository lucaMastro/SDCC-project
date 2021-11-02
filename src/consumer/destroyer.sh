#!/bin/sh

root=`pwd`/init_infrastructure

# delete mess-bucket objects:
aws s3 rm s3://message-bucket-sdcc-20-21 --recursive

cd $root 
echo 'yes' | terraform destroy

