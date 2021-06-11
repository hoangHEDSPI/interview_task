def suffixMatch(s: str) -> int:
    match =len(s)
    i = 1
    j = 1
    while (i < len(s)):
        if s[i] != s[0]:
            i += 1
            if i == len(s):
                break
        if s[i] == s[0]:
            i += 1
            match += 1
            while i < len(s) and s[i] == s[j]:
                match += 1
                i += 1
                j += 1
            j = 1
    return match


if __name__ == '__main__':
    s = 'abcabc'
    s = [''.join(str(i)) for i in range(100000)]
    for i in range(10):
        print(suffixMatch(s))

