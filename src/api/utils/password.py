from passlib.context import CryptContext


bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Password:
    def hash(password):
        return bcrypt.hash(password)

    def compare(password, hash):
        return bcrypt.verify(password, hash, "bcrypt")