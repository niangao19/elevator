import elevator

class Controler :
    def __init__( self, e1_floor = 1, e2_floor = 1 ) :
        self.e1 = elevator.Elevator( "1", e1_floor )
        self.e2 = elevator.Elevator( "2", e2_floor )

    def move( self ,current : int, dst : int ) :
        if abs(self.e1.display_floor(False) - current) <= abs(self.e1.display_floor(False)  - current) :
            print( self.e1.display_floor(False) )
            self.e1.move( self.e1.display_floor(False),  current - self.e1.display_floor(False) )
            self.e1.move( self.e1.display_floor(False),  dst - current)

        else :
            self.e2.move( self.e2.display_floor(False),  current - self.e2.display_floor(False) )

            self.e2.move( self.e2.display_floor(False),  dst - current)



if __name__ == "__main__":
    e1_floor = int(input( "input current e1_floor : " ))
    e2_floor = int(input( "input current e2_floor : " ))    
    controler = Controler( e1_floor, e2_floor)

    while True :
        cur_floor = int( input( "which floor are you on : ") )
        if cur_floor <= 0 or cur_floor > 10 :
            print( "Floors between 1st to 10th")
            continue
        dst = int( input( "Which floor do you want to go to? : " ) )
        if dst <= 0 or dst> 10 :
            print( "Floors between 1st to 10th")
            continue
        controler.move( cur_floor, dst )

