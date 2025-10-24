import unittest
import elevator

class Test(unittest.TestCase):
    elevator = elevator.Elevator( "1" )
    test_floor = [ [1,2] , [ 3, 5], [ 8 , -2], [6, -4 ] ]
    ans = [ 3, 8, 6, 2]
    def test_0(self) :
        i = self.elevator.display_floor() 
        self.assertEqual(i, 1)
    pass

    def test_1(self) :
        for i in range( 0 , len(self.test_floor) ) :
            floor = self.elevator.move( self.test_floor[i][0], self.test_floor[i][1] )
            self.assertEqual(floor, floor)
        pass

if __name__ == "__main__":
    unittest.main()