class Player():
    def __init__(self, name, back_number):
        self.name = name
        self.back_number = back_number
        
    def print_stat(self):
        print(f"This is {self.__class__.__name__} Class")
        print(f"Player Name: {self.name}")
        print(f"Back Number: {self.back_number}")
        
        
class SoccerPlayer(Player):
    def __init__(self, name, back_number, position):
        super().__init__(name, back_number)
        self.position = position
        
    def print_stat(self):
        super().print_stat()
        # print("This is Soccer Player Class")
        # print(f"Player Name: {self.name}")
        # print(f"Back Number: {self.back_number}")
        print(f"Position: {self.position}")
        
        
class BaseballPlayer(Player):
    def __init__(self, name, back_number, position, avg):
        super().__init__(name, back_number)
        self.position = position
        self.avg = avg
        
    def print_stat(self):
        super().print_stat()
        # print("This is Baseball Player Class")
        # print(f"Player Name: {self.name}")
        # print(f"Back Number: {self.back_number}")
        print(f"Position: {self.position}")
        print(f"Batting Average: {self.avg}")