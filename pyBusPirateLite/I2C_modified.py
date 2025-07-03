# I2C.py (Modified version with get_config_summary)

class I2C:
    def __init__(self, connection):
        self.connection = connection
        self.enabled = False  # Track state manually
        self.last_action = None

    def enable(self):
        self.connection.write(b"\x02")
        response = self.connection.read(1)
        success = response == b"\x01"
        if success:
            self.enabled = True
            self.last_action = "Enabled I2C"
        return success

    def disable(self):
        self.connection.write(b"\x00")
        response = self.connection.read(1)
        success = response == b"\x01"
        if success:
            self.enabled = False
            self.last_action = "Disabled I2C"
        return success

    def start(self):
        self.connection.write(b"\x02")
        self.last_action = "Start condition sent"

    def stop(self):
        self.connection.write(b"\x03")
        self.last_action = "Stop condition sent"

    def write(self, data):
        self.connection.write(bytes([0x10 | len(data)]))
        self.connection.write(data)
        self.last_action = f"Wrote {len(data)} byte(s)"
        return self.connection.read(1)

    def get_config_summary(self):
        return {
            "enabled": self.enabled,
            "last_action": self.last_action
        }
