import datetime
import csv
import random
import subprocess

# This function uses PybricksDev to push the program to the brick
# filename: The name of the file to push. Should be in the same directory as the program.
# returns the output of the program, all prints in the program are captured.
def uploadProgramToHub(filename):
    process = subprocess.run(["pybricksdev", "run", "ble", filename], capture_output=True, ) 
    if process == None:
        print("Could not launch pybricksdev")
    print (process.stdout)
    return str(process.stdout)

def extractAndWriteTimings(output):
    def _extractRunTime(line, outputDict):
        startOfRunTime = line.find("RunTime : ", 0, len(line))
        #"Time for arm change time(ms):"
        if (startOfRunTime == -1):
            return

        runName = line[startOfRunTime + len("RunTime : "):startOfRunTime + len("RunTime : ") + 4]
        startOfRunTiming = startOfRunTime + len("RunTime : ") + 7
        runTime = line[startOfRunTiming : len(line)]
        outputDict[runName] = runTime
        return

    def _extractAttachmentChangeTime(line, outputDict):
        startOfRunTime = line.find("AttachmentChange: ", 0, len(line))
        if (startOfRunTime == -1):
            return

        changeName = line[startOfRunTime + len("AttachmentChange: "): startOfRunTime + len("AttachmentChange: ") + 23]
        changeTimingStart = startOfRunTime + len("AttachmentChange: ") + len("Run0To1AttachmentChange") + 1
        changeTiming = line[changeTimingStart : len(line)]
        outputDict[changeName] = changeTiming
        return

    f = open("timings.csv", "a")
    writer = csv.DictWriter(f, ["DateTime", 
        "run0", "Run0To1AttachmentChange", 
        "run1", "Run1To2AttachmentChange", 
        "run2", "Run2To3AttachmentChange", 
        "run3", "Run3To4AttachmentChange", 
        "run4", "Run4To5AttachmentChange", 
        "run5", "Run5To6AttachmentChange", 
        "run6", "Run6To7AttachmentChange", 
        "run7", "Run7To8AttachmentChange", 
        "run8"], delimiter=',')

    lines = output.splitlines()
    outputDict = {}
    outputDict["DateTime"] = datetime.datetime.now()
    for line in lines:
        _extractRunTime(line, outputDict)
        _extractAttachmentChangeTime(line, outputDict)
        
    print(outputDict)        
    writer.writerow(outputDict)
    f.flush()
    f.close()

    '''
    start = 0
    startOfRunTime = _extractOneTime(output, "RunTime : ", start, len(output))
    #"Time for arm change time(ms):"
    if (startOfRunTime == -1)
        startOfRunTime = len("RunTime : ")
    return
    '''

def runMainAndCaptureTimings():
    print("launching program")
    output = uploadProgramToHub('C:\\Users\\Vivek\\FLL\\MasterPiece\\StateWithNewRunOrder\\main.py')
    extractAndWriteTimings(output)

runMainAndCaptureTimings()
#extractAndWriteTimings("Searching for any hub with Pybricks service...\r\nvoltage: 7982\r\nAttachmentChange: Run1To2AttachmentChange:17610\r\nRunTime : run2 : 2303\r\nAttachmentChange: Run2To3AttachmentChange:2589\r\nRunTime : run3 : 10143\r\nAttachmentChange: Run3To4AttachmentChange:3589\r\nRunTime : run4 : 3183\r\nAttachmentChange: Run4To5AttachmentChange:7989\r\nRunTime : run5 : 8914\r\nAttachmentChange: Run5To6AttachmentChange:6089\r\nRunTime : run6 : 29088\r\nThe program was stopped (SystemExit).\r\n")
#extractAndWriteTimings("Searching for any hub with Pybricks service...\r\nvoltage: 8004\r\nAttachmentChange: Run1To2AttachmentChange:929\r\nRunTime : run2 : 2303\r\nAttachmentChange: Run2To3AttachmentChange:12049\r\nMissed black line catch infront of the scene change.\r\nThe program was stopped (SystemExit).\r\n")