from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["POSTGRESQL_USER"]
password = os.environ["POSTGRESQL_PASSWORD"]
host = os.environ["POSTGRESQL_HOST"]
database = os.environ["POSTGRESQL_DATABASE"]

DATABASE_CONNECTION_URI = f'postgres://{ user }:{ password }@{ host }/{ database }'
print(DATABASE_CONNECTION_URI)
