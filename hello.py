import hashlib
import random


def hello(name: str = "World") -> str:
    return f"Hello, {name}!"


def random_hash() -> str:
    """Return a random SHA-256 hash."""
    return hashlib.sha256(str(random.random()).encode()).hexdigest()


if __name__ == "__main__":
    print(hello())
    print(random_hash())
