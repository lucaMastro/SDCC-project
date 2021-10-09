#!/bin/sh

root=`pwd`
buckets_creator_path=$root/buckets-creator
infrastructure_path=$root/infrastructure 
src_path=$root/python_source
db_path=$root/db 

#-------------------------------------------
# creating db:
cd $db_path
terraform init
echo 'yes' | terraform apply

# db initialization 
db_host=`aws rds describe-db-instances --filters "Name=engine,Values=mysql" \
  --query "*[].[Endpoint.Address]"  --output text`

mysql -h $db_host -P 3306 -u admin \
  --password='sdcc-db-admin' < $db_path/db_generation.sql


#-------------------------------------------
# creating buckets:
cd $buckets_creator_path 
terraform init
echo 'yes' | terraform apply


#-------------------------------------------
# add sources:
cd $src_path 

# clean of previously updated source zip
terraform init
echo 'yes' | terraform destroy

# removing local version
rm sources.zip 2>/dev/null

#saving db_host in a variable for python usage
echo "DB_HOST = '$db_host'" > host.py 

cd $src_path/package-mysql-connector 
zip -r ../sources.zip .
cd ..
zip -g sources.zip *.py 

terraform init
echo 'yes' | terraform apply

#-------------------------------------------
# creating infrastucture:
cd $infrastructure_path 
terraform init
# destroying previous lambdas
echo 'yes' | terraform destroy
echo 'yes' | terraform apply

