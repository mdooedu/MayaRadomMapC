import maya.cmds as cmds
import random


def RandomCount(a, b):

    x = float(random.randrange(a, b))
    y = float(random.randrange(a, b))
    z = float(random.randrange(a, b))

    return x, y, z


def GetVecVal(count):
    xLocation = []
    yLocation = []
    zLocation = []

    if count < 3:
        print("좌표 갯수가 부족합니다")

    else:

        temp = range(1, count + 1)
        list(temp)

        for i in temp:
            xLocation.append(cmds.getAttr("pCube" + str(i) + ".translateX"))
            yLocation.append(cmds.getAttr("pCube" + str(i) + ".translateY"))
            zLocation.append(cmds.getAttr("pCube" + str(i) + ".translateZ"))

    return xLocation, yLocation, zLocation


def GetRangeVec(xyzlist):

    xRange = sorted(xyzlist[0])
    yRange = sorted(xyzlist[1])
    zRange = sorted(xyzlist[2])

    return xRange, yRange, zRange


print(GetRangeVec(GetVecVal(4)))
