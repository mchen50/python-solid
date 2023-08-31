from abc import ABC, abstractmethod


# Make your classes depend on abstractions rather than on concrete implementations like BackEnd.
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"


class FrontEnd:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


if __name__ == "__main__":
    database = Database()
    front_end = FrontEnd(database)
    front_end.display_data()

    api = API()
    front_end = FrontEnd(api)
    front_end.display_data()
