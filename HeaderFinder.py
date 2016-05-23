import re
import binascii
import os
import sys
import multiprocessing

def worker(inpFile, arrHeaders):
    with open(inpFile, "rb") as file:
        intLen = 0
        arrOutPutData = []
        while intLen < os.path.getsize(inpFile):
            content = file.read(10000000)  # Block = 10 000 000 bytes -> Size can be increased or decreased, depending on memory resources
            intLen = intLen + 10000000
            for k in range(0, len(arrHeaders)):
                for m in re.finditer(re.compile(re.escape(arrHeaders[k])), content):
                    arrOutPutData.append([hex(m.start() + intLen - 10000000), arrHeaders[k]])
                    print("\n" + hex(m.start() + intLen - 10000000))
                    print(arrHeaders[k])
        file.close()
    strOutputFile = "Results - " + inpFile + ".txt"
    with open(strOutputFile, "w") as fOutPut:
        fOutPut.write("Hex\tValue\tLocation\n")
        for j in range(0, len(arrOutPutData)):
            fOutPut.write(binascii.hexlify(arrOutPutData[j][1]).decode('windows-1252') + "\t" + arrOutPutData[j][1].decode('windows-1252') + "\t" + str(arrOutPutData[j][0]) + "\n")

if __name__ == '__main__':
    with open("ALLheaders.txt", "r") as f:
        arrHeaders = f.read().splitlines()

    for i in range(0,len(arrHeaders)):
        arrHeaders[i] = binascii.unhexlify(arrHeaders[i])

    #print("Database with known Magic Values loaded:\n" + str(arrHeaders))

    arrFiles = []
    if len(sys.argv) > 1:
        for i in range(1,len(sys.argv)):
            arrFiles.append(str(sys.argv[i]))
    else:
        arrFiles.append(str(input("\nPlease input a valid filename:\n")))

    workers = []
    intfinishedWorkers = 0

    while (intfinishedWorkers < len(arrFiles)):
        if len(multiprocessing.active_children()) < 8: #change this value to the amount of processes your PC is able to handle
            p = multiprocessing.Process(target=worker, args=(arrFiles[intfinishedWorkers],arrHeaders,))
            workers.append(p)
            p.start()
            intfinishedWorkers = intfinishedWorkers + 1

        
