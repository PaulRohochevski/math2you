"""
Алгоритм шифрования ГОСТ 28147-89.

В режиме простой замены произвести первый цикл шифрования блока открытого текста Т0 и вычислить числа:
1. а (число в накопителе N1)
2. b (число в накопителе N2)

Исходные данные:
1. ключ К0 = 10000111010101010010101000011010
2. Блок открытого текста Т0 = 0010011110110101001100011000011011001011111001111101010110001100
"""

t: str = '0010011110110101001100011000011011001011111001111101010110001100'
k: str = '10000111010101010010101000011010'

a: str = t[:32]  # First part of 't'
b: str = t[32:]  # Second part of 't'

print("T='{}'\na(base 2)={} | a(base 10)={}\nb(base 2)={} | b(base 10)={}\nk(base 2)={} | k(base 10)={}\n"
      "".format(t, a, int(a, 2), b, int(b, 2), k, int(k, 2)))


def block_cm1(a_base_2: str, k_base_2: str) -> int:
    base_2_32: int = 2 ** 32
    a_k_sum: int = int(a_base_2, 2) + int(k_base_2, 2)

    if a_k_sum >= base_2_32:
        a_k_sum -= base_2_32

    return a_k_sum


def block_cm2(r_base_2: str, b_base_2: str) -> int:
    assert len(r_base_2) == len(b_base_2), 'expected the same length'

    result: list = ['0' if r_base_2[i] == b_base_2[i] else '1' for i in range(len(r_base_2))]

    return int(''.join(result), 2)


res_of_cm1: int = block_cm1(a, k)
res_of_cm1_base_2: str = '{:032b}'.format(res_of_cm1)
print("Result of 'CM1 Block': base_2={} | base_10={}\n".format(res_of_cm1, res_of_cm1_base_2))

print("Partition with step equal to 4 position:")
s8, s7, s6, s5, s4, s3, s2, s1 = (res_of_cm1_base_2[i: i + 4] for i in range(0, 29, 4))

print("s8(base 2)={} | s8(base 10)={}\ns7(base 2)={} | s7(base 10)={}\ns6(base 2)={} | s6(base 10)={}\n"
      "s5(base 2)={} | s5(base 10)={}\ns4(base 2)={} | s4(base 10)={}\ns3(base 2)={} | s3(base 10)={}\n"
      "s2(base 2)={} | s2(base 10)={}\ns1(base 2)={} | s1(base 10)={}\n"
      "".format(s8, int(s8, 2), s7, int(s7, 2), s6, int(s6, 2), s5, int(s5, 2), s4, int(s4, 2), s3, int(s3, 2), s2,
                int(s2, 2), s1, int(s1, 2)))

print("Substitution 's' values from the table...")
substituted_s8: str = "{0:04b}".format(7)
substituted_s7: str = "{0:04b}".format(9)
substituted_s6: str = "{0:04b}".format(7)
substituted_s5: str = "{0:04b}".format(12)
substituted_s4: str = "{0:04b}".format(11)
substituted_s3: str = "{0:04b}".format(1)
substituted_s2: str = "{0:04b}".format(0)
substituted_s1: str = "{0:04b}".format(0)

s = substituted_s8 + substituted_s7 + substituted_s6 + substituted_s5 + substituted_s4 + substituted_s3 + \
    substituted_s2 + substituted_s1
print("Concatenation substituted result: s(base 2)={} | s(base 10)={}\n".format(s, int(s, 2)))

r: str = s[11:] + s[:11]
print("Shifted left 11 positions: r(base 2)={} | r(on base 10)={}\n".format(r, int(r, 2)))

new_a: int = block_cm2(r, b)
new_a_base_2: str = '{:032b}'.format(new_a)
print("Result of 'CM2 Block': a(base 2)={} | a(base 10)={}\n".format(new_a_base_2, new_a))

new_b = int(a, 2)
print("First loop completed, a={} | b={}".format(new_a, new_b))
