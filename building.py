import datetime


class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.date.today()

    def purchase(self, name):
        self.owner = name

    def __str__(self):
        return (f"owner = {self.owner}, address = {self.address}, stories = {self.stories}")

    def solution_sentence(self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.")
