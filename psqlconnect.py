import psycopg2

conn = psycopg2.connect(database="db_name",
                        host="db_host",
                        user="db_username",
                        password="db_password",
                        port="db_port")
