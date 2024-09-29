
string = input()
num_words = {}

for s in string:
    ss = s.upper()
    if ss in num_words:
        num_words[ss] += 1
    else:
        num_words[ss] = 1

words = []
cnt = 0
for k, v in num_words.items():
    if v > cnt:
        cnt = v
        words = [k]
    elif v == cnt:
        words.append(k)

print('?' if len(words) > 1 else words[0])