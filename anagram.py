input = [
    "abccde",
    "aaabbb",
    "ab",
    "abc",
    "mnop",
    "xyyx",
    "xaxbbbxx",
    "fdhlvosfpafhalll",
]


def anagram(s):
    if len(s) % 2 != 0:
        return -1
    n = int(len(s) / 2)
    aux1, aux2 = s[:n], s[n:]
    aux3 = [i for i in aux1 if i not in aux2]
    aux4 = [i for i in aux2 if i not in aux1]
    print(aux1, aux2, aux3, aux4)
    return len(aux3)

s = 'xyyx'
s = 'fdhlvosfpafhalll'
print(anagram(s))

