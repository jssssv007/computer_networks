for _ in range(int(input())):
    was = dict()
    s = input()

    n = len(s)
    for i in range(n):
        for j in range(i, n):
            cur = s[i:j + 1]
            cur = ''.join(sorted(cur))
            was[cur] = was.get(cur,0) + 1
    print(was)

    ans = 0
    for x in was:
        print(x)
        v = was[x]
        ans += (v * (v - 1)) // 2

    print(ans)