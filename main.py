from person import input_guest
from util import save_data, get_data, delete_data
import time
import datetime


ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
time = datetime.datetime.fromtimestamp(ts).strftime("%I:%M %p")


def printLine():
    print("=" * 33)


def print_header() -> None:
    printLine()
    print("     HOTEL RESERVATION SYSTEM")
    printLine()


def main_menu() -> None:
    print("\n")
    printLine()
    print("Please choose from the following: ")
    printLine()
    print("A - View All Reservations")
    print("B - Make Reservation")
    print("C - Delete Reservation")
    print("D - Generate Report")
    print("E - Exit the program")


class Hotel:
    def __init__(self):
        self.__adult_rate: int = 500
        self.__children_rate: int = 300
        self.hotel_db: str = "hotel.txt"

    def get_adult_rate(self) -> int:
        return self.__adult_rate

    def get_child_rate(self) -> int:
        return self.__children_rate

    def get_user_input(self) -> str:

        while True:
            main_menu()
            user_input: str = input("\nEnter from the choices above: ").lower()
            if user_input in ["a", "b", "c", "d", "e"]:
                return user_input
            else:
                print("Please choose from the choices only!!!")

    def make_reservation(self) -> None:
        guest_data_tuple = input_guest()
        adult_total: int = guest_data_tuple[3] * self.get_adult_rate()
        child_total: int = guest_data_tuple[4] * self.get_child_rate()
        grand_total: int = adult_total + child_total

        guest_data: tuple = (
            guest_data_tuple + (adult_total, child_total, grand_total) + (time, date)
        )
        guest_data: str = ", ".join(str(item) for item in guest_data)

        if save_data(self.hotel_db, guest_data):
            print("DONE!!!")

    def view_reservation(self, view: str) -> None:
        reservations: list = get_data(self.hotel_db)
        for reservation in reservations:
            if view == "reservation":
                reserve_list: list = [
                    element.strip() for element in reservation[:6] + reservation[-2:]
                ]
            else:
                reserve_list: list = [element.strip() for element in reservation]

            print(*reserve_list, sep=", ")

    def delete_reservation(self) -> None:
        guest_name = input("\nEnter the exact name to delete reservation: ")
        if delete_data(self.hotel_db, guest_name):
            print(f"Guest {guest_name} delete from the system.")

    def main(self) -> None:
        print_header()

        while True:
            user_input = self.get_user_input()
            match user_input:
                case "a":
                    print("\nView All Reservations")
                    self.view_reservation("reservation")
                case "b":
                    print("\nMake Reservation")
                    self.make_reservation()
                case "c":
                    print("Delete Reservation")
                    self.view_reservation("report")
                    self.delete_reservation()
                case "d":
                    print("\nGenerate Report")
                    self.view_reservation("report")
                case "e":
                    break

        print("Thank You.")


if __name__ == "__main__":
    hotel = Hotel()
    hotel.main()
