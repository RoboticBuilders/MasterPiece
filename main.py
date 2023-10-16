from Utilities import *
from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *

def driver():
    waitForLeftButtonPress()
    run1()
    waitForLeftButtonPress()
    run2()
    waitForLeftButtonPress()
    run1()
    run3()
    waitForLeftButtonPress()
    run4()
    waitForLeftButtonPress()
    run5()

driver()