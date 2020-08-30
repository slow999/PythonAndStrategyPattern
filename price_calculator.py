# This is a fun example

from abc import ABC, abstractmethod


class Tshirt():
    def __init__(self, strategy=None, price=0):
        self._strategy = strategy
        self._price = price

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    @property
    def price(self):
        return self._price

    @price.getter
    def price(self):
        if self._strategy:
            return self._strategy.calculate_price(self._price)
        else:
            return self._price


class PriceStrategy(ABC):
    @abstractmethod
    def calculate_price(self, price):
        pass


class PremiumPriceStrategy(PriceStrategy):
    def calculate_price(self, price):
        return price * 0.5


class ListingPriceStrategy(PriceStrategy):
    def calculate_price(self, price):
        return price * 1.2


class GiveawayPriceStrategy(PriceStrategy):
    def calculate_price(self, price):
        return price * 0


if __name__ == '__main__':
    # client

    tshirt = Tshirt(price=20)

    print('Original price', tshirt.price)

    tshirt.strategy = PremiumPriceStrategy()
    print('Premium price: ', tshirt.price)

    tshirt.strategy = ListingPriceStrategy()
    print('Listing price: ', tshirt.price)

    tshirt.strategy = GiveawayPriceStrategy()
    print('Giveaway price: ', tshirt.price)