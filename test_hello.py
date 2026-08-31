from hello import hello, random_hash


def test_hello():
    assert hello() == "Hello, World!"


def test_random_hash():
    # Debe generar un hash de 64 caracteres y distinto cada vez
    h1 = random_hash()
    h2 = random_hash()
    assert len(h1) == 64
    assert h1 != h2
