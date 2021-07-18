import sys
ans = 0

for text in sys.stdin:
    text = text.split()
    ans += (len(text))

print(ans)