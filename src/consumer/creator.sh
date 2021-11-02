#!/bin/sh

root=`pwd`/init_infrastructure
src_path=$root/python_source
db_path=$root/db 

#-------------------------------------------

# removing local version
rm $root/sources.zip 2>/dev/null

cd $src_path/package-mysql-connector 
zip -r $root/sources.zip . 
cd ..
zip -g $root/sources.zip *.py 

cd $root
terraform init
echo 'yes' | terraform apply

# db initialization 
db_host=`aws rds describe-db-instances --filters "Name=engine,Values=mysql" \
  --query "*[].[Endpoint.Address]"  --output text`

mysql -h $db_host -P 3306 -u admin \
  --password='sdcc-db-admin' < $db_path/db_generation.sql


