def function1() -> str:
    return "{} {}".format("Jan", "Schaffranek")


def function2() -> str:
    return f'{"Jan"} {"Schaffranek"}'


def main() -> None:
    function1()
    function2()


if __name__ == "__main__":
    main()
