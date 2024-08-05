import pytest


class TestCard:
    def test_generate_card(self, card_example):
        assert len(card_example.numbers) == 3  # Должно быть 3 строки
        assert all(len(row) == 5 for row in card_example.numbers)  # Каждая строка должна содержать 5 чисел
        assert len(set(num for row in card_example.numbers for num in row)) == 15  # Должно быть 15 уникальных чисел

    def test_remove_number(self, card_example):
        number_to_remove = card_example.numbers[0][0]  # Берем первое число из первой строки
        assert card_example.remove_number(number_to_remove)  # Удаление должно быть успешным
        assert number_to_remove not in card_example.numbers[0]  # Число должно быть удалено
        assert card_example.remove_number(99) is False  # Удаление несуществующего числа должно вернуть False

    def test_is_winner(self, card_example):
        assert not card_example.is_winner()  # Изначально карточка не должна быть выигрышной
        for i in range(3):
            for j in range(5):
                card_example.numbers[i][j] = "-"  # Заменяем все числа на "-"
        assert card_example.is_winner()  # Теперь карточка должна быть выигрышной


if __name__ == "__main__":
    pytest.main()
