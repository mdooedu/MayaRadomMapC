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


def GetVecValLoc(count):  # count는 입력 받을 큐브의 전체 갯수
    xLocation = []
    yLocation = []
    zLocation = []

    if count < 3:
        print("좌표 갯수가 부족합니다")

    else:

        temp = range(1, count + 1)
        list(temp)

        for i in temp:  # pCube의 좌표값을 번호대호 반환 반복
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

        i += 1  # x, y, z 인덱스 반복 출력을 위한 for문 상수값

        a = listofvalran[p][0]  # 정렬 된 리스트의 인덱스 0번값; 최소값 a로 반환
        b = listofvalran[p][-1]  # 정렬된 리스트의 인덱스 -1값; 최대값 b로 반환

        if i == 1:
            xRange.append(a)
            xRange.append(b)
        elif i == 2:
            yRange.append(a)
            yRange.append(b)
        else:
            zRange.append(a)
            zRange.append(b)

    xRange.sort()
    yRange.sort()
    zRange.sort()

    return xRange, yRange, zRange


def ReturnFinalRnaVal(listreturn, targetcount):
    uniDB = []  # xyz값을 순서대로 오브젝트상 적용 가능하게 통합

    x = count_gen(listreturn[0][0], listreturn[0][1], targetcount)
    y = count_gen(listreturn[1][0], listreturn[1][1], targetcount)
    z = count_gen(listreturn[2][0], listreturn[2][1], targetcount)

    for i in range(targetcount):
        uniDB.append([x[0], y[0], z[0]])  # 좌표값 리스트 0번 인덱스 오브젝트 인덱스 0번으로 입력
        x.pop(0)  # 입력한 인덱스 값 삭제 추후 pop값 로그로 출력모듈 도입
        y.pop(0)
        z.pop(0)

    return uniDB


def GetVecValScl():  # frequency는 반환 받은 스케일의 중간값 반환
    xyzScale = []
    temp = [1, 2]

    for i in temp:  # pCube의 좌표값을 번호대호 반환 반복
        p = cmds.getAttr("Scale" + str(i) + ".scale")  # 좌표값이 튜플로 입력됨
        xyzScale.append(list(p[0]))  # 튜플로 들어온 좌표값 리스트로 변환후 반환

    return xyzScale  # 리스트 안의 리스트로 반환


def xyzRange(xyzListRe):
    xyzRangeList = []
    temp = range(3)  # xyz값 모두를 반환 하기 위한 상수

    for i in temp:
        a = xyzListRe[0][0]
        b = xyzListRe[1][0]
        xyzRangeList.append([a, b])  # xyz값 각각 세트로 반환

    return xyzRangeList


def mainFucLoc(a, temp):

    b = GetVecValLoc(a)  # 오브젝트의 좌표값을 호출받음
    c = GetRangeVec(b)  # 입력 받은 값 정렬
    d = ReturnRange(c)  # 정령된 리스트의 최소 최댓값 반환
    asResul = ReturnFinalRnaVal(d, temp)  # 랜덤값 생성 및 반환 후 오브젝트 입력값 순서로 재정렬

    return asResul  # 최종 범위 내에서 랜덤 생성된 값 x, y, z순으로 인덱스 반환


def mainFucScl(temp):
    a = GetVecValScl()  # 오브젝트 스케일값 입력후 반환
    b = xyzRange(a)  # 입력받은 스케일 좌표값 x,y,z 범위로 정렬
    c = ReturnFinalRnaVal(b, temp)

    return c  # 랜덤하게 반환된 좌표값 반환


def CreatRelocate(ranlocin, ransclin, temp):
    RanLocDB = ranlocin
    RanSclDB = ransclin

    for i in range(1, temp + 1):
        temp += 1
        iNam = str(i)
        nam = "pSphere"
        tran = nam + iNam + '.translate'
        rot = nam + iNam + '.rotate'
        sca = nam + iNam + '.scale'
        set_01 = RanLocDB.pop([0][0])
        set_02 = RanSclDB.pop([0][0])
        print(set_01, set_02)
        x_01 = set_01[0]
        y_01 = set_01[1]
        z_01 = set_01[2]
        x_02 = set_02[0]
        y_02 = set_02[1]
        z_02 = set_02[2]

        cmds.duplicate(nam + iNam)
        cmds.setAttr(tran, x_01, y_01, z_01)
        cmds.setAttr(sca, x_02, y_02, z_02)

    return

