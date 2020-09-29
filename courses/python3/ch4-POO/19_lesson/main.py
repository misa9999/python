"""
Animal -> breathe
    Wolf(Animal) -> breathe / howl
        Dog(Wolf) -> breathe / howl / bark
"""
from classes.wolf import Wolf


w1 = Wolf()
w1.call_howl_method()
