import random

def play_game():
    choices = ["Камень", "Ножницы", "Бумага"]
    
    user_choice = input("Выберите Камень, Ножницы или Бумага: ").capitalize()
    while user_choice not in choices:
        print("Некорректный выбор. Попробуйте снова.")
        user_choice = input("Выберите Камень, Ножницы или Бумага: ").capitalize()
    
    computer_choice = random.choice(choices)
    
    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "Камень" and computer_choice == "Ножницы") or \
         (user_choice == "Ножницы" and computer_choice == "Бумага") or \
         (user_choice == "Бумага" and computer_choice == "Камень"):
        print("Вы победили!")
    else:
        print("Вы проиграли.")
    

play_game()