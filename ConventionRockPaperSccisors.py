#камінь ножниці бумага

import random

def rps():
    print('Welcome to the RPS Game!')    #привітання
    user_score = 0
    comp_score = 0

    while True:
        print('Choose: 1 - Rock, 2 - Paper, 3 - Scissors')     #вибір можливих ходів
        user_choice = input('Your choice: ')

        if user_choice not in ['1', '2', '3']:    #робите вибір
            print('Invalid choice, try again.')
            continue

        comp_choice = random.choice(['1', '2', '3'])    #комп'ютер робить вибір
        print('Computer chose:', comp_choice)

        if user_choice == comp_choice:     #якщо вибір одинаковий то це нічия
            print('It\'s a draw!')
        elif (user_choice == '1' and comp_choice == '3') or \
             (user_choice == '2' and comp_choice == '1') or \
             (user_choice == '3' and comp_choice == '2'):    # якщо я вибираю 1 а кмп. 3 або я вибираю 2 а комп.1 або  я вибираю 3 а комп.2 то в цему випадку виграю я
            print('You win!')
            user_score += 1    #і мені прибавляється 1 бал
        else:
            print('You lose!')   # в інших випадках я програла
            comp_score += 1   # і бал зараховується комп'ютерові

        print('Score: You:', user_score, 'Computer:', comp_score)    # показ результату

        again = input('Play again? (y/n): ')   # питаємо чи ми хочемо продовжити гру
        if again.lower() != 'y':
            print('Final score: You:', user_score, 'Computer:', comp_score)
            print('Thanks for playing! Goodbye!')  #подяка за гру
            break    # кінець

rps()   # виклик функції