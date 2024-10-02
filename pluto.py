import sys
import os

cwd = os.getcwd()
dev = False
files = {}

def nameOverwrite(index):
    if ((index + 1) < len(sys.argv) and sys.argv[index + 1][0] != "-"):
        files[sys.argv[index - 1]] = sys.argv[index + 1]
        sys.argv.pop(index + 1), sys.argv.pop(index), sys.argv.pop(index - 1)
        if (dev): print(":) | Name overwrite confirmed.")
    else:
        if (dev): print(":( | Arguments passed incorrectly.")

def checkFile(filePath):
    if (os.path.isfile(filePath)):
        if (dev): print(":) | Found file '%s'." % filePath)
        return 1
    else:
        if (dev): print(":( | Missing File '%s'." % filePath)
        return 0

def checkType(fileName):
    if (fileName.split(".")[1] == "ipynb"):
        if (dev): print(":) | File '%s' is a Jupyter Notebook." % fileName)
        return 1
    else:
        if (dev): print(":( | File '%s' is not a Jupyter Notebook." % fileName)
        return 0

def createFolder(folderPath):
    if not os.path.isdir(folderPath):
        os.makedirs(folderPath)
        if (dev): print(":) | Directory '%s' created." % folderPath)
    else:
        if (dev): print(":( | Directory '%s' already exists." % folderPath)

def getFileName(fileName):
    return fileName.split(".")[0]

def process():
    global dev
    print("-- | Welcome to Pluto.")

    # REMOVE PLUTO.PY FROM ARGS
    sys.argv.pop(0)

    # DEV FLAG CHECK AND REMOVAL FIRST
    for arg in sys.argv:
        if (arg == "-d"): dev = True, print("-- | Dev mode has been enabled."), sys.argv.pop(sys.argv.index(arg))

    # OVERWRITE FLAG CHECK AND REMOVAL
    for arg in range(len(sys.argv) - 1, -1, -1):
        print(sys.argv[arg])
        if (arg == "-o"): nameOverwrite(sys.argv.index(arg))

    # OTHER FILES CHECK
    for arg in sys.argv:
        if (arg != "" or arg != None): files[arg] = ""

    for arg in files:
        if (checkFile(cwd + "\\" + arg) and checkType(arg)):
            createFolder(getFileName(arg))

    print("-- | Files: ", files)


# '''
# for item in my_dict:  
#     print(item) #KEY
#     print(my_dict[item]) #VALUE
# '''

process()