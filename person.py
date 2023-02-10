from dataclasses import dataclass, astuple


@dataclass
class Person:
    __name: str
    __address: str
    __contact: str

    @property
    def get_info(self) -> tuple:
        return astuple(self)


@dataclass
class Guest(Person):
    __number_adults: int
    __number_children: int


def get_input() -> tuple:
    name: str = input("Enter guest name: ")
    address: str = input("Enter guest address: ")
    contact: str = input("Enter guest contact number: ")
    number_adults: int = int(input("Enter number of adults: "))
    number_children: int = int(input("Enter number of children: "))
    return (name, address, contact, number_adults, number_children)


def input_guest() -> tuple:
    name, address, contact, number_adults, number_children = get_input()
    guest = Guest(name, address, contact, number_adults, number_children)
    return guest.get_info


if __name__ == "__main__":
    guest = Guest("Juniven", "Surigao City", "234235234234", 2, 3)
    infos = guest.get_info
    print(infos)
