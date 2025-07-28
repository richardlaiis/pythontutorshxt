def capitalize(word):
    return chr(ord(word[0]) - 32) + word[1:]

ans = " ".join(map(capitalize, input().split(' ')))

print(ans)
