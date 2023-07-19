import time

from sqlalchemy import create_engine
from sqlalchemy.engine.url import make_url

# from CTFd.config import Config
ssl_args = {'ssl_ca': "/etc/ssl/certs/ca-certificate.crt"}
url = make_url("mysql+pymysql://doadmin:AVNS_3FAey36iLsJn1WiG1po@bcf23-mysql-do-user-14379091-0.b.db.ondigitalocean.com:25060/defaultdb")
# Ignore sqlite databases
if url.drivername.startswith("sqlite"):
    exit(0)

# Null out the database so raw_connection doesnt error if it doesnt exist
# CTFd will create the database if it doesnt exist
# url.database = None

# Wait for the database server to be available
engine = create_engine(url, connect_args=ssl_args)
print(url)

print(f"Waiting for {url.host} to be ready")
while True:
    try:
        x = engine.raw_connection()
        print(x)
        break
    except Exception as e:
        print(e)
        print(".", end="", flush=True)
        time.sleep(1)

print(f"{url.host} is ready")
time.sleep(1)
