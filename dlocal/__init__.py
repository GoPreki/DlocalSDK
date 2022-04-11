from dlocal.utils.requests import Keys


def init(x_trans_key, x_login, secret_key, test: bool):
    Keys.X_TRANS_KEY = x_trans_key
    Keys.X_LOGIN = x_login
    Keys.SECRET_KEY = secret_key
    Keys.TEST = test
