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
        temp = random.uniform(a, b)  # VerT return num
        db.append(temp)
    return db


# 큐브 1~n 값의 로케이션 값 저장 후 반환


def GetVecVal(count):  # count는 입력 받을 큐브의 전체 갯수
    xLocation = []
    yLocation = []
    zLocation = []

    if count < 3:
        print("좌표 갯수가 부족합니다")

    else:

        temp = range(1, count + 1)
        list(temp)

        for i in temp:  # pCube의 좌표값은 번호대호 반환 반복
            xLocation.append(cmds.getAttr("pCube" + str(i) + ".translateX"))
            yLocation.append(cmds.getAttr("pCube" + str(i) + ".translateY"))
            zLocation.append(cmds.getAttr("pCube" + str(i) + ".translateZ"))

    return xLocation, yLocation, zLocation

# 입력받은 리스트 정렬후 반환


def GetRangeVec(xyzlist):  # xyzlist는 큐브의 좌표값을 1번부터 N번까지 순서대로 반환 받은 값

    xRange = sorted(xyzlist[0])
    yRange = sorted(xyzlist[1])
    zRange = sorted(xyzlist[2])

    return xRange, yRange, zRange


def ReturnRange(listofvalran):  # listofvalran은 정렬 된 큐브의 좌표값

    xRange = []
    yRange = []
    zRange = []
    i = 0

    for p in range(3):  # x,y,z 리스트의 최소 최대값 반환

        i += 1

        a = listofvalran[p][0]
        b = listofvalran[p][-1]

        if i == 1:
            xRange.append(a)
            xRange.append(b)
        elif i == 2:
            yRange.append(a)
            yRange.append(b)
        else:
            zRange.append(a)
            zRange.append(b)

    return xRange, yRange, zRange


def ReturnFinalRnaVal(listreturn, targetcount):  # xyz값을 순서대로 오브젝트상 적용 가능하게 통합
    uniDB = []

    x = count_gen(listreturn[0][0], listreturn[0][1], targetcount)
    y = count_gen(listreturn[1][0], listreturn[1][1], targetcount)
    z = count_gen(listreturn[2][0], listreturn[2][1], targetcount)

    for i in range(targetcount):
        uniDB.append([x[0], y[0], z[0]])
        x.pop(0)
        y.pop(0)
        z.pop(0)

    return uniDB


def mainfuc(a, temp):
    b = GetVecVal(a)  # 오브젝트의 좌표값을 호출받음
    c = GetRangeVec(b)  # 입력 받은 값 정렬
    d = ReturnRange(c)  # 정령된 리스트의 최소 최댓값 반환
    asResul = ReturnFinalRnaVal(d, temp)  # 랜덤값 생성 및 반환 후 오브젝트 입력값 순서로 재정렬

    return asResul


a = int(input("값을 입력받을 큐브의 갯수"))
temp = int(input("만들 좌표의 갯수\n"))

print(mainfuc(a, temp))
