

def main():
    menu = {}
    total = 0

    print("Вітаємо в ресторані!")
    print("Введіть страву та її ціну.")

    while True:

        name = input("назва страви: ")
        if name.lower() == 'stop':
            break

        try:

            menu[name] = float(input(f"Введіть ціну для '{name}': "))
        except ValueError:
            print("введіть справжне число для ціни.")
            continue


    for price in menu.values():
        total += price

    print("\nВаше замовлення:")
    for name, price in menu.items():
        print(f"{name}: {price:.2f} грн")

    print(f"\nЗагальна сума замовлення: {total:.2f} грн")


if __name__ == "__main__":
    main()