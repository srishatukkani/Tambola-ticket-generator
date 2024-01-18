from peewee import *
# db = PostgresqlDatabase('tambola', user='newuser1', password='password', host='localhost', port = 5432)

db = PostgresqlDatabase('db_name', user='siri', password='siri', host='localhost', port = 5432)

# CREATE TABLE tambola_ticket (
#     id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
#     set_id VARCHAR(50) NOT NULL,
#     ticket_number INTEGER NOT NULL,
#     row1 VARCHAR(50) NOT NULL,
#     row2 VARCHAR(50) NOT NULL,
#     row3 VARCHAR(50) NOT NULL
# );

"""
psql postgres:
    CREATE ROLE siri WITH LOGIN PASSWORD 'siri';
    ALTER ROLE siri CREATEDB;
    \q
psql postgres -U siri:

"""