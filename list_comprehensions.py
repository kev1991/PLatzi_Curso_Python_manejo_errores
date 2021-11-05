def kev():
    # squares = []
    # for k in range (1,101):
    #     if k % 3 != 1:
    #         squares.append(k**2)
    # print(squares)

    squares = [k for k in range(1,100000) if k % 36 == 0]
    print(squares)

    squares = [k for k in range(1,100000) if k % 4 == 0 and k % 6 == 0 and k % 9 == 0]
    print(squares)

if __name__ == "__main__":
    kev()