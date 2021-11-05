def kev ():
    my_list = [1, "Hello", True, 4.5]
    my_dict ={"first_mane": "Kebin", "last_name":"Martinez"}

    super_list = [
        {"first_mane": "Kebin0", "last_name":"Martinez0"},
        {"first_mane": "maria", "last_name":"romero"},
        {"first_mane": "jose", "last_name":"tapias"},
        {"first_mane": "luiz", "last_name":"camchon"}
    ]

    super_dict ={
        "natural_nums":[1, 2, 3, 4],
        "integral_nums":[-2, -1, 0, 1, 2],
        "floating":[2.5, 5.21, 0.88, 7.81, 9.2]
    }

    # for key, value in super_dict.items():
    #     print(key, "-", value)

    for item in super_list:
        print(item["first_mane"], "-", item["last_name"])

if __name__ == "__main__":
    kev()