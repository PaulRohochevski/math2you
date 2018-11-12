"""
Асимметричая криптосистема RSA

Сгенерировать ключи для шифрования и расшифрования:
1. Открытый К0 (public)
2. Секретный Кс (private)
3. Зашифровать сообщение М и расшифровать его
4. Убедиться , что ключи сгенерированы правильно.

Исходные данные:
1. простое число Р = 17
2. простое число Q = 29
3. сообщение М = 3
"""

P: int = 17
Q: int = 29
M: int = 3

n = P * Q
print("Initial values: P={} | Q={} | M={} | n=P*Q={}".format(P, Q, M, n))


def gcd(a: int, b: int) -> int:
    while b != 0:
        remainder = a % b
        a, b = b, remainder

    return a


def phi(n: int):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1

    return amount


phi_res: int = phi(n)
print("Euler's function result: {}".format(phi_res))

check_phi_res: int = (P - 1) * (Q - 1)
print("Check that result counted by 'phi' method equal to '(P - 1) * (Q - 1)' result: {} == {}".format(phi_res,
                                                                                                       check_phi_res))
assert phi_res == check_phi_res


def get_public_key(phi_value: int):
    result = None

    for k in range(2, phi_value):
        if gcd(k, phi_value) == 1:
            result = k
            break

    assert result is not None, "Couldn't generate public key"

    return result


public_key: int = get_public_key(phi_res)
print("Generated public key: {}".format(public_key))


def get_private_key(pub_key: int, phi_val: int):
    priv: int = 1

    while (pub_key * priv) % phi_val != 1:
        priv += 1
        assert priv < 1e16, "Too many iterations: {}".format(priv)

    return priv


private_key: int = get_private_key(public_key, phi_res)
print("Generated private key: {}".format(private_key))

encrypted_msg: int = (M ** public_key) % n
print("Encrypted message: {}".format(encrypted_msg))

decrypted_msg: int = (encrypted_msg ** private_key) % n
print("Decrypted message: {}".format(decrypted_msg))
