import jwt

from settings.config import Config

config = Config()


def encode_jwt(
        payload: dict,
        private_key: str = config.jwt.private_key_path.read_text(),
        algorithm: str = config.jwt.algorithm
):
    return jwt.encode(
        payload,
        private_key,
        algorithm=algorithm
    )


def decode_jwt(
        token: str | bytes  ,
        public_key: str = config.jwt.public_key_path.read_text(),
        algorithm: str = config.jwt.algorithm
):
    return jwt.decode(
        token,
        public_key,
        algorithms=[algorithm]
    )
