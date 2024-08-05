import random


def generate_card():
    unique_numbers = random.sample(range(1, 91), 15)  # Генерируем 15 уникальных чисел
    card = []
    for i in range(3):
        row = sorted(unique_numbers[i * 5:(i + 1) * 5])  # Разбиваем на 3 строки по 5 чисел
        card.append(row)
    return card


class Card:
    def __init__(self):
        self.numbers = generate_card()

    def remove_number(self, number):
        for i, row in enumerate(self.numbers):
            if number in row:
                index = row.index(number)
                row[index] = "-"
                return True
        return False

    def is_winner(self):
        return all(all(num == "-" for num in row) for row in self.numbers)

    def display(self):
        for row in self.numbers:
            display_row = []
            for num in row:
                display_row.append(f"{num:>2}")
            print(" | ".join(display_row))
        print("--------------------------")


class LottoGame:
    def __init__(self):
        self.buckets = list(range(1, 91))
        random.shuffle(self.buckets)
        self.player_card = Card()
        self.computer_card = Card()
        self.current_bucket_index = 0

    def draw_bucket(self):
        if self.current_bucket_index < len(self.buckets):
            return self.buckets[self.current_bucket_index]
        return None

    def player_turn(self):
        bucket = self.draw_bucket()
        print(f"Новый бочонок: {bucket} (осталось {len(self.buckets) - self.current_bucket_index - 1})")
        print("------ Ваша карточка -----")
        self.player_card.display()
        print("-- Карточка компьютера ---")
        self.computer_card.display()

        choice = input("Удалить цифру? (y/n): ").strip().lower()
        if choice == 'y':
            if not self.player_card.remove_number(bucket):
                print("Цифры нет на карточке! Вы проиграли!")
                return False
        else:
            if self.player_card.remove_number(bucket):
                print("Цифра есть на карточке! Вы проиграли!")
                return False
        return True

    def computer_turn(self):
        bucket = self.draw_bucket()
        if self.computer_card.remove_number(bucket):
            print("Компьютер удалил число.")
        else:
            print("Компьютер пропустил число.")

    def play(self):
        while self.current_bucket_index < len(self.buckets):
            if not self.player_turn():
                break
            self.computer_turn()
            self.current_bucket_index += 1

            if self.player_card.is_winner():
                print("Поздравляем! Вы выиграли!")
                break
            if self.computer_card.is_winner():
                print("Компьютер выиграл!")
                break


if __name__ == "__main__":
    game = LottoGame()
    game.play()
