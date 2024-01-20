from flask import Flask
from flask import request
from werkzeug.exceptions import Unauthorized

from config import Config
from extensions import ext_database, ext_celery, ext_migrate
from extensions.ext_database import db


class IPv6AddrApp(Flask):
    pass


def create_app() -> Flask:
    ipv6_addr_app = IPv6AddrApp(__name__)
    ipv6_addr_app.config.from_object(Config)
    ext_migrate.init(ipv6_addr_app, db)
    ext_database.init_app(ipv6_addr_app)
    ext_celery.init_app(ipv6_addr_app)
    return ipv6_addr_app


app = create_app()
celery = app.extensions["celery"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
