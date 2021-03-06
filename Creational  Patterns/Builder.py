

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def product_part_a(self) -> None:
        pass
    
    @abstractmethod
    def product_part_b(self) -> None:
        pass

    @abstractmethod
    def product_part_c(self) -> None:
        pass
    

class ConcerteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product
    
    def product_part_a(self) -> None:
        self._product.add("PartA1")
    
    def product_part_b(self) -> None:
        self._product.add("PartB1")

    def product_part_c(self) -> None:
        self._product.add("PartC1")


class Product1():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")

    
class Director:
    def __init__(self) -> None:
        self._builder = None
    
    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.product_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.product_part_a()
        self.builder.product_part_b()
        self.builder.product_part_c()


if __name__ == "__main__": 
    director = Director()
    builder = ConcerteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")


    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Customer Product: ")
    builder.product_part_a()
    builder.product_part_b()
    builder.product.list_parts()