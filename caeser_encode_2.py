text = input("請輸入想要加密的字串: ")
d = int(input("請輸入位移值 d: "))

alphabet = "".join([chr(i) for i in range(97, 123)])

d = d % 26
new_alphabet = alphabet[d:] + alphabet[:d]

print(alphabet)
print(new_alphabet)

doc = dict()
for i in range(26):
    doc[alphabet[i]] = new_alphabet[i]

ans = "".join(doc[i] for i in text)
print(ans)
