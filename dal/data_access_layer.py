class DataAccessLayer:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            return ""

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)
