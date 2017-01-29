import os
import time
import subprocess
import sys

fileList = []
rootdir = input("Root Dir: ")
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        theFile = os.path.join(root, file)
        fileName, fileExtension = os.path.splitext(theFile)
        if fileExtension.lower() in ('.avi', '.divx', '.flv', '.m4v', '.mov', '.mpg', '.mpeg', '.wmv'):
            print('Adding', theFile)
            fileList.append(theFile)

runstr = '/usr/bin/HandBrakeCLI -i {0} -o {1} --preset="Normal" --two-pass --turbo'
runlist = []
runlist.append("/usr/bin/HandBrakeCLI")
runlist.append("-i")
runlist.append("inFile")
runlist.append("-o")
runlist.append("outFile")
runlist.append("--preset=\"Normal\"")
runlist.append("-e")
runlist.append("x264")
runlist.append("--vfr")
#runlist.append("--two-pass")
#runlist.append("--turbo")

print('=======--------=======')

while fileList:
    inFile = fileList.pop()
    fileName, fileExtension = os.path.splitext(inFile)
    outFile = fileName+'.mkv'
    runlist[2] = inFile
    runlist[4] = outFile

    print('Processing', inFile)
    process = subprocess.run(runlist)
    print(process.returncode)
    time.sleep(5)
    break
    print('Removing', inFile)
    #os.remove(inFile)