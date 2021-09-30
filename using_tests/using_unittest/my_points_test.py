import unittest # one of several unit test tools

from my_points import Point # this is the unit to be tested

class testPoint(unittest.TestCase):
    # set up before each test
    def setUp(self):
        # this code runs before EACH test
        self.point = Point(3,5) # we make sure each test is NOT dependent on any other test

    # declare each test here
    def testMoveByA(self):
        '''Test the moveBy method with x and y values'''
        self.point.moveBy(5,2)
        # make an assertion
        self.assertEqual( self.point.display(), (8,7) )
    def testMoveByB(self):
        '''Test the moveBy method with -ve x and y values'''
        self.point.moveBy(-5,-2)
        # make an assertion
        self.assertEqual( self.point.display(), (-2,3) )
    def testMoveByC(self):
        self.point.moveBy(dy=9)
        self.assertEqual( self.point.display(), (3,14) )
    def testPointCounter(self): # careful - this depends on the numer of tests!!
        '''test that we can accurately count the number of point instances'''
        self.assertGreater(Point.points, 0) # how many would we expect?
    def testHypot(self):
        '''Derive the hypotenuse from x and y'''
        # self.point.moveBy(0,-1) # leaves the point at (3,4)
        r = self.point.hypot()
        self.assertAlmostEqual(r, 5.83, places=2) # 5.830951894845301
    def testPosNegHypot(self):
        '''The positive hypot should exual a negative hypot'''
        self.pos_h = Point(3,4)
        self.neg_h = Point(-3,-4)
        self.assertAlmostEqual( self.pos_h.hypot(), self.neg_h.hypot() )
    def testExceptionRaised(self):
        '''if x or y are non integer, we expect a TypeError exception'''
        with self.assertRaises(TypeError):
            Point('3',4) # string not int

if __name__ == '__main__':
    unittest.main() # this invokes our tests