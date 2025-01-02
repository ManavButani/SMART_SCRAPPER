from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def sum(a, b):
    # sum function

    return a + b


def sub(x, y):
    return x - y
