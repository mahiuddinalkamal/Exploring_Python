from dataclasses import dataclass
from functools import reduce
from typing import List
from item import Item


@dataclass
class Basket(object):
    items: List[Item]

    def total(self):
        if len(self.items) > 0:
            return reduce(lambda subtotal, item: subtotal + item.unit_price * item.quantity, self.items, 0)
            #return self.items[0].unit_price * self.items[0].quantity
        return 0


