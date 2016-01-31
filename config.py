from getpass import getuser
import platform

user = getuser()


# class Config:
#     CFG_FILE = 'config.Config'


# class TestConfig(Config):
#     CFG_FILE = 'config.TestConfig'


class DevConfig:  # (Config):  # Config commented out above and needs to be defined for a finished product
    APPLICATION_ROOT = None
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + 'C:/Users/{}/PycharmProjects/iq_db/sqlite-test.db'.format(user)
    BASE_URL = "http://{}:5004".format(platform.node())
    # RESULTS_DIR = "C:/Users/Shawn/PycharmProjects".format(user)
    # CFG_FILE = 'config.DevConfig'
    # DOWNLOAD_DIR = url
