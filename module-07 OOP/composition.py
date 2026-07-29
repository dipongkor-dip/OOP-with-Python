class Engine:
    def __init__(self):
        pass

    def start(self):
        return "engine started"


class Driver:
    def __init__(self):
        pass


# car 'has a' engine
class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()


# Example 2
class CPU:
    def __init__(self, cores):
        self.cores = cores


class RAM:
    def __init__(self, size):
        self.size = size


class HardDrive:
    def __init__(self, capacity):
        self.capacity = capacity


# Computer 'has a' cpu
# Computer 'has a' ram
# Computer 'has a' hard disc
class Computer:
    def __init__(self, cores, size, capacity):
        self.cpu = CPU(cores)
        self.ram = RAM(size)
        self.hard_disc = HardDrive(capacity)


mac = Computer(8, 16, 256)
