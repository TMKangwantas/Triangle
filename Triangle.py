def cleanUpLines(file):
    newFileList = []
    for line in file:
        newFileList.append(line.strip().strip("\n").split(" "))
    return newFileList

def replaceAndRemoveLastLine(bottomRow, secondToBottomRow):
    replacementRow = []
    for i in range(len(secondToBottomRow)):
        replacementRow.append(max(int(secondToBottomRow[i]) + int(bottomRow[i]), int(secondToBottomRow[i]) + int(bottomRow[i+1])))
    return replacementRow

openFile = open("triangle.txt", "r")
triangle = cleanUpLines(openFile.readlines())

for i in range(len(triangle)-2, -1, -1):
    bottomRow = triangle[i+1]
    secondToBottomRow = triangle[i]
    triangle.pop()
    triangle[i] = replaceAndRemoveLastLine(bottomRow, secondToBottomRow)

print("The maximum sum of the triangle is: " + str(*triangle[0]))

openFile.close()