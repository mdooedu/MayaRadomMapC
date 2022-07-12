import maya.cmds as cmds
import random


def RandomCount(a, b):

    LocationVal = []
    ScalVal = []
    RotationVal = []

    x = float(random.randrange(a, b))
    y = float(random.randrange(a, b))
    z = float(random.randrange(a, b))

    return x, y, z


# 큐브 1~n 값의 로케이션 값 저장 후 반환


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

# 입력받은 리스트 정령후 반환


def GetRangeVec(xyzlist):

    xRange = sorted(xyzlist[0])
    yRange = sorted(xyzlist[1])
    zRange = sorted(xyzlist[2])

    return xRange, yRange, zRange


print(GetRangeVec(GetVecVal(4)))
