from dataclasses import dataclass


@dataclass
class Item(object):
    unit_price: float
    quantity: int
