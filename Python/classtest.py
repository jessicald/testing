#!/usr/bin/env python2.7

class Test:
    """ The following variables are considered "static" because Test has them with or without instantiation.
    They aren't true static in the C++ sense because if an instance of Test assigns to them,
    Test and other/new instances of Test maintain the following values.
    """
    sets = 1
    lamps = 2

    def __init__(self):
        traps = 5  # Destroyed at the end of __init__
        nets = 6  # Destroyed at the end of __init__
        self.traps = 5
        self.nets = 6

    def test_func_1(self):
        """This function does nothing to the static variables because the following are local to it."""
        sets = 3
        lamps = 4

    def test_func_2(self):
        self.sets = 3
        self.lamps = 4

    def test_func_3(self):
        self.traps = 7
        self.nets = 8

"""The following line dies at Test.traps because traps is not static to Test."""
# print "sets = %s, lamps = %s, traps = %s, nets = %s" % (Test.sets, Test.lamps, Test.traps, Test.nets)
test = Test()
print "sets = %s, lamps = %s, traps = %s, nets = %s" % (test.sets, test.lamps, test.traps, test.nets)
test.test_func_1()
print "sets = %s, lamps = %s, traps = %s, nets = %s" % (test.sets, test.lamps, test.traps, test.nets)
test.test_func_2()
print "sets = %s, lamps = %s, traps = %s, nets = %s" % (test.sets, test.lamps, test.traps, test.nets)
test.test_func_3()
print "sets = %s, lamps = %s, traps = %s, nets = %s" % (test.sets, test.lamps, test.traps, test.nets)
