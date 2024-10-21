import os

class Config:
    username = os.getenv("DB_USERNAME", username)
    password = os.getenv("DB_PASSWORD", password)
    dbname = os.getenv("DB_NAME", dbname)
    host = os.getenv("DB_HOST", host)
    port = os.getenv("DB_PORT", port)


username = ''
password = ''
dbname = ''
host = ''
port = ''