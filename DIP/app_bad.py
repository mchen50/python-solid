# This violates DIP because the FrontEnd class depends on the BackEnd class
# and its concrete implementation.Both classes are tightly coupled.
# This coupling can lead to scalability issues.
class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"


class FrontEnd:
    def __init__(self, back_end: BackEnd):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)


if __name__ == "__main__":
    back_end = BackEnd()
    front_end = FrontEnd(back_end)
    front_end.display_data()
