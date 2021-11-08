#!/bin/bash

echo "Give me the aws_access_key: "
read aws_access_key

echo "Give me the aws_secret_access_key: "
read aws_secret_access_key 

echo "Give me the aws_access_key: "
read aws_session_token

echo "Give me the aws_default_region: "
read aws_default_region

echo "AWS_ACCESS_KEY_ID=$aws_access_key" > .env
echo "AWS_SECRET_ACCESS_KEY=$aws_secret_access_key" >> .env
echo "AWS_SESSION_TOKEN=$aws_session_token" >> .env
echo "AWS_DEFAULT_REGION=$aws_default_region" >> .env
echo "use_credentials_file=False" >> .env

