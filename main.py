from calculator.calculator import add, subtract, multiply, divide


def repl():
    print("Simple Calculator Started!")

    while True:
        cmd = input(">>> ")

        if cmd == "quit":
            break

        op, a, b = cmd.split()
        a, b = float(a), float(b)

        if op == "add":
            print(add(a, b))
        elif op == "sub":
            print(subtract(a, b))
        elif op == "mul":
            print(multiply(a, b))
        elif op == "div":
            print(divide(a, b))


if __name__ == "__main__":
    repl()
