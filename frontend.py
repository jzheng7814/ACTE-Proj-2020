for i in [((i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)) for i in range(0, 20, 2) for j in range(0, 4, 2)]:
    print(i)