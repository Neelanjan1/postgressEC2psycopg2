# postgressEC2psycopg2
Python script to write and fetch DB entry in postgres running in an EC2 instance using psycopg library.

## EC2 free trial instance t2.micro
Enable security group for 22 and postgres port 5432
Ubuntu

## SSH into EC2 and install/setup postgress
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib
sudo service postgresql start

## I will be connecting to postgress from external IP so allow external connections
Refer to this file : /etc/postgresql/<version>/main/pg_hba.conf
  - refer authentication records and append accordingly - in my case I have allowed all external connection in
    security group and also will allow all connections to postgress
  - restart service

## postgress running - login and create DB
Activity list:
  Create a DB
  Create user and assign password
  Assign privilege to the user to the DB operations
  Use same credentials to write into DB
  Fetch info from DB viewer

Referred - https://stackoverflow.com/questions/67276391/why-am-i-getting-a-permission-denied-error-for-schema-public-on-pgadmin-4

\\ Break \\
Troubleshooting with error in Postgres.
## From local/external system create + write into DB + read from table
For this we use available library psycopg
Install in local system - pip install psycopg2-binary
Write script for create table + write into DB


2024-09-03 18:58:15.972 UTC [4160] CONTEXT:  line 134 of configuration file "/etc/postgresql/16/main/pg_hba.conf"
2024-09-03 18:58:15.972 UTC [4160] FATAL:  could not load /etc/postgresql/16/main/pg_hba.conf
2024-09-03 18:58:15.974 UTC [4160] LOG:  database system is shut down

https://medium:
  com/@pantaanish/setting-up-postgresql-on-an-ec2-instance-a-step-by-step-guide-9be2e3348fdb:
