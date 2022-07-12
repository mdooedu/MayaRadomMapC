import maya.cmds as cmds
import random


def count_gen(a, b, target_count):
    # TargetCount = int(input("target count:\n"))  # count of object to making
    # a = float(input("범위변수_1:\n"))
    # b = float(input("범위변수_2:\n"))
    db = []
    i = 0
    for i in range(target_count):
        i += 1
        x = random.uniform(a, b)  # VerT return num
        y = random.uniform(a, b)  # VerT return num
        z = random.uniform(a, b)  # VerT return num
        db.append([x, y, z])
    return db


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


def ReturnRange(listofvalran):

    a = listofvalran[0][0]
    b = listofvalran[0][-1]

    return a, b


a = GetVecVal(4)
print(a)
b = GetRangeVec(a)
print(b)
c = ReturnRange(b)
print(c)
d = c[-1]
f = c[0]

print(count_gen(f, d, 10))
