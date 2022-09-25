# 127-> 1111111?
def decimal_to_binary(n):
    if n == 0:
        return "0"
    num = 0
    binaries = []
    while n > 0:
        binaries.append(n % 2)
        n //= 2
    binaries.reverse()
    return "".join(map(str, binaries))

print(decimal_to_binary(127))
print(decimal_to_binary(128))
print(decimal_to_binary(1))
print(decimal_to_binary(0))
