
total = 0

def add_to_cart(price):
    global total
    total += price

add_to_cart(150)
add_to_cart(200)
add_to_cart(50)

print(f"Загальна сума покупок: {total} грн.")




glasses_drunk = 0

def drink_water():
    global glasses_drunk



    glasses_drunk += 1
    print(f"Ви випили склянку води. Загальна кількість: {glasses_drunk}")


    if glasses_drunk >= 8:
        print("Ви вже досягли денного мінімуму!")



drink_water()
drink_water()
drink_water()
drink_water()
drink_water()
drink_water()
drink_water()
drink_water()
drink_water()




steps_count = 0


def add_steps(count):
    global steps_count

    steps_count += count
    print(f" додали {count} кроків. Загальна кількість кроків: {steps_count}")


    if steps_count >= 10000:
        print("Ви досягли своєї мети на сьогодні!")



add_steps(7000)
add_steps(200)
add_steps(3000)
add_steps(400)
add_steps(5000)






budget = 6000

def spend_money(amount):
    global budget

    budget -= amount
    print(f"Ви витратили {amount} грн. Залишок бюджету: {budget} грн.")


    if budget < 0:
        print("Попередження: Ви перевищили бюджет!")


spend_money(300)
spend_money(5000)
spend_money(700)
spend_money(10)
spend_money(100)
spend_money(400)
