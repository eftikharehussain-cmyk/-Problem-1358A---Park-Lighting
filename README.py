# -Problem-1358A---Park-Lighting
for _ in range(int(input())):
    n, m = map(int, input().split())
    tot = n * m
    x = tot % 2
    y = tot // 2
    print(x + y)
