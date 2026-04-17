#main simulation engine, responsible for generating days and managing the flow of the simulation
class DayGenerator:
    def __init__(self):
        self.day = 1

    def next_day(self):
        self.day += 1
        return self.day

    def get_day(self):
        return self.day
