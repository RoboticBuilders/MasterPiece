from Utilities import *

def CollectLoadData():
    drive_base.straight(distance = 450, wait = False) # 45 cm
    stall_detect.collectAndLogLoadData(10, 1000)

CollectLoadData()