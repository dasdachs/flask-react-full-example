import hashlib

from flask import current_app

from inventory import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def hash_password(self, plain_text_password: str):
        self.password = self._gen_hash(plain_text_password)

    def compare_password(self, plain_text_password: str) -> None:
        hashed_password = self._gen_hash(plain_text_password)

        return self.password == hashed_password

    def _gen_hash(self, plain_text_password: str) -> str:
        """
        > Key derivation and key stretching algorithms are designed for secure
        > password hashing. Naive algorithms such as sha1(password) are not
        > resistant against brute-force attacks. A good password hashing function
        > must be tunable, slow, and include a salt.

        We use the `pbkdf2_hmac` method, with a sha256 hashing algorithm and use the
        secret key as the `salt`. An even better approach would be to use a library like
        bycrypt.
        """
        hashed_pwd = hashlib.pbkdf2_hmac(
            "sha256",
            plain_text_password.encode(),
            current_app.config.get("SECRET_KEY").encode(),
            1000,
        )

        return hashed_pwd.hex()

    def __repr__(self) -> str:
        return f"<User name={self.username} password='plain_password'>"
