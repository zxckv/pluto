import sys
import os
import json

cwd = os.getcwd()
dev = False
files = {}
content = {}

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
    if not (os.path.isdir(folderPath) or os.path.isdir(files[folderPath])):
        if (files[folderPath] != ''):
            os.makedirs(files[folderPath])
        else:
            os.makedirs(getFileName(folderPath))
        if (dev):
            if (files[folderPath] != ''): print(":) | Directory '%s' created." % files[folderPath])
            else: print(":) | Directory '%s' created." % folderPath)
        return 1
    else:
        if (dev): 
            if (files[folderPath] != ''): print(":( | Directory '%s' already exists." % files[folderPath])
            else: print(":( | Directory '%s' already exists." % folderPath)
        return 0

def getFileName(fileName):
    return fileName.split(".")[0]

# LOAD THE NOTEBOOK AS JSON DATA AND EXTRACT NEEDED INFO
def loadData(fileName):
    file = open(fileName, 'r')

    data = json.load(file)['cells']
    tempContent = []

    for item in data:
        if (item['cell_type'] == 'markdown'):
            tempContent.append(item['source'])
    
    content[fileName] = tempContent

    file.close()
    return 0

def populateFolder(fileName):
    if (files[fileName] != ''):
        path = files[fileName]
    else:
        path = getFileName(fileName)

    index = 1
    for secs in content[fileName]:
        createFile(path, secs, index)
        index += 1

    return 0

def createFile(fileName, data, index):
    file = open(fileName + "/" + fileName + "-" + str(index) + ".py", "w")

    file.write("'''\n")
    
    for seg in data:
        file.write(seg)

    file.write("\n'''\n\n")

    file.close()

    return 0

def main():
    global dev
    print("-- | Welcome to Pluto.")

    # REMOVE PLUTO FROM ARGS
    sys.argv.pop(0)

    # DEV FLAG CHECK AND REMOVAL FIRST
    for arg in sys.argv:
        if (arg == "-d"): dev = True, print("-- | Dev mode has been enabled."), sys.argv.pop(sys.argv.index(arg))

    # OVERWRITE FLAG CHECK AND REMOVAL
    for arg in sys.argv:
        if (arg == "-o"): nameOverwrite(sys.argv.index(arg))

    # OTHER FILES CHECK
    for arg in sys.argv:
        if (arg != "" or arg != None): files[arg] = ""

    if (dev): print("-- | Files: ", files)

    for arg in files:
        if (checkFile(cwd + "//" + arg) and checkType(arg)):
            if (createFolder(arg)):
                loadData(arg)
                populateFolder(arg)
    

# '''
# for item in my_dict:  
#     print(item) #KEY
#     print(my_dict[item]) #VALUE
# '''

main()