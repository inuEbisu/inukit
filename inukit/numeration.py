#给一个int 将其转换为radix进制数的形式并返回str
def num(inp: int, radix: int) -> str:
    tmp = ''
    d = inp
    while True:
        n = d % radix
        d = d // radix
        tmp = f'{n}' + tmp
        if d == 0:
            break
    return tmp