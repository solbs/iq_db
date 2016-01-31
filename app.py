from flask import Flask
from models import db
from views import iq_views


def create_app(config):
    iq_app = Flask(__name__)
    iq_app.config.from_object(config)
    iq_app.secret_key = '1ll#%@%^LJ2sd#lj23@$^-'

    with iq_app.app_context():
        db.init_app(iq_app)
        db.create_all()

    iq_app.register_blueprint(iq_views)
    return iq_app


if __name__ == '__main__':
    app = create_app('config.DevConfig')
    app.run(port=3589, debug=True, host='0.0.0.0', threaded=True)
