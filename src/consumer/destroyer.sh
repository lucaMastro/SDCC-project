#!/bin/sh

root=`pwd`/init_infrastructure

# setting default options:
use_shared_file='y'

for i in "$@"; do
  if [[ "$i" == "-env_var" ]]; then
    use_shared_file='n'
    continue
  fi
done

if [[ "$use_shared_file" == "n" ]]; then
  # configuration of env-variables
  echo "Give me the aws_access_key: "
  read AWS_ACCESS_KEY_ID
  export AWS_ACCESS_KEY_ID

  echo "Give me the aws_secret_access_key: "
  read AWS_SECRET_ACCESS_KEY 
  export AWS_SECRET_ACCESS_KEY

  echo "Give me the aws_access_key: "
  read AWS_SESSION_TOKEN
  export AWS_SESSION_TOKEN

  echo "Give me the aws_default_region: "
  read AWS_DEFAULT_REGION
  export AWS_DEFAULT_REGION
fi

# delete mess-bucket objects:
aws s3 rm s3://message-bucket-sdcc-20-21 --recursive

cd $root 
echo 'yes' | terraform destroy

