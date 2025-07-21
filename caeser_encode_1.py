def convert(ch, d):
    diff = (ord(ch) - ord('a') + d) % 26
    return chr(ord('a') + diff)

text = input("請輸入想要加密的字串: ")
d = int(input("請輸入位移值 d: "))

ans = "".join([convert(ch, d) for ch in text])

print(ans)
