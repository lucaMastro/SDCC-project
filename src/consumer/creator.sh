#!/bin/sh

root=`pwd`/init_infrastructure
src_path=$root/python_source
db_path=$root/db 

#-------------------------------------------
# setting default options:
use_shared_file='y'
create_db='y'

for i in "$@"; do
  if [[ "$i" == "-no_db" ]]; then
    create_db='n'
    continue
  elif [[ "$i" == "-env_var" ]]; then
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


# removing local version
rm $root/sources.zip 2>/dev/null

cd $src_path/package-mysql-connector 
zip -r $root/sources.zip . 
cd ..
zip -g $root/sources.zip *.py 

cd $root
terraform init
echo 'yes' | terraform apply

# checking if re-init db:
if [[ "$create_db" == "y" ]]; then
  # db initialization 
  db_host=`aws rds describe-db-instances --filters "Name=engine,Values=mysql" \
    --query "*[].[Endpoint.Address]"  --output text`

  mysql -h $db_host -P 3306 -u admin \
    --password='sdcc-db-admin' < $db_path/db_generation.sql

fi

