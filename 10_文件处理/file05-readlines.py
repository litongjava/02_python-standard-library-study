with open(r"e.txt", "r", encoding="utf-8") as f:
    while True:
        fragment = f.readline()
        if not fragment:
            break
        else:
            print(fragment, end="")
