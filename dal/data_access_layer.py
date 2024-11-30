class DataAccessLayer:
    def __init__(self, filename:str) -> None:
        self.filename = filename

    def read_data(self) -> str:
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            return ""

    def write_data(self, data:str) -> None:
        with open(self.filename, 'w') as file:
            file.write(data)
