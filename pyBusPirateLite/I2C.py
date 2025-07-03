# I2C.py (Original version)

class I2C:
    def __init__(self, connection):
        self.connection = connection

    def enable(self):
        self.connection.write(b"\x02")
        response = self.connection.read(1)
        return response == b"\x01"

    def disable(self):
        self.connection.write(b"\x00")
        response = self.connection.read(1)
        return response == b"\x01"

    def start(self):
        self.connection.write(b"\x02")

    def stop(self):
        self.connection.write(b"\x03")

    def write(self, data):
        self.connection.write(bytes([0x10 | len(data)]))
        self.connection.write(data)
        return self.connection.read(1)
