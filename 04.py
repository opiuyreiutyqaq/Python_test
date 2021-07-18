ans = ""

text = input()
text = text.split()
for i in text:
    ans += i[0]

print(ans)
