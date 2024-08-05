from pytest import fixture

from game.Loto import Card, LottoGame


@fixture
def card_example():
    return Card()
