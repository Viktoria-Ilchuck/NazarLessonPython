class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price} грн"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):

        self.products.append(product)
        print(f"{product.name} додано в кошик.")

    def remove_product(self, product_name):

        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product_name} видалено з кошика.")
                return
        print("Товар не знайдений в кошику.")

    def get_total(self):

        return sum(product.price for product in self.products)

    def contents(self):

        if not self.products:
            print("Кошик порожній.")
        else:
            print("Ваш кошик:")
            for product in self.products:
                print(product)


def main():
    cart = Cart()

    product1 = Product("хурма", 200, "сухофрукти")
    product2 = Product("рамен", 150, "їжа")
    product3 = Product("байка", 500, "одяг")
    product4 = Product("наклейки", 100, "аніме")
    product5 = Product("дубайский шоколад", 300, "солодощі")
    product6 = Product("акрілова фарба", 300, "художні матеріали")
    product7 = Product("шампунь", 120, "косметика")
    product8 = Product("смартфон", 39000, "техніка")
    product9 = Product("піаніно", 23000, "музичні інструменти")

    products_list = [
        product1,
        product2,
        product3,
        product4,
        product5,
        product6,
        product7,
        product8,
        product9
    ]

    while True:
        print("\n1. Додати товар в кошик")
        print("2. Видалити товар з кошика")
        print("3. Переглянути кошик")
        print("4. Загальна сума")
        print("5. Оформити замовлення")
        print("6. Вийти")

        try:
            choice = int(input("Оберіть дію: "))

            if choice == 1:
                print("\nДоступні товари:")

                for i in range(len(products_list)):
                    print(f"{i + 1}. {products_list[i]}")
                product_choice = int(input("Оберіть товар для додавання: ")) - 1

                if 0 <= product_choice < len(products_list):
                    cart.add_product(products_list[product_choice])
                else:
                    print("Невірний вибір товару.")

            elif choice == 2:
                product_name = input("Введіть назву товару для видалення: ")
                cart.remove_product(product_name)

            elif choice == 3:
                cart.contents()

            elif choice == 4:
                print(f"Загальна сума: {cart.get_total()} грн")

            elif choice == 5:
                if cart.products:
                    print("Замовлення оформлено!")
                    print(f"Загальна сума замовлення: {cart.get_total()} грн")
                    break
                else:
                    print("Ваш кошик порожній. Не можна оформити замовлення.")

            elif choice == 6:
                print("Пока!")
                break

            else:
                print("Невірний вибір")

        except ValueError:
            print("введіть правильне число")


if __name__ == "__main__":
    main()

