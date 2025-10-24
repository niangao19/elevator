class Elevator:
    def __init__(self, name, current_floor=1):
        self.name = name
        self.current_floor = current_floor
        self.target_floor = None
        self.direction = 0
        self.queue = []  


    def add_request(self, floor):
        self.queue.append(floor)
        print(f"{self.name} received new request → floor {floor}")

    def display_floor( self) :
        print( f' current floor is : {self.current_floor}' )
        return self.current_floor
    
    def move(self , current: int, floor: int) :
        self.current_floor = current + floor
        self.display_floor()
        




