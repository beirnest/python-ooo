"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        "Create serial with a starting number"
        self.start = start
        self.serial = start
    
    def generate(self):
        "Return serial number and increase serial by 1"
        current_serial = self.serial
        self.serial = self.serial + 1
        return current_serial

    def reset(self):
        "Reset serial counter"
        self.serial = self.start
    
