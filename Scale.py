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


def GetVecVal():  # frequency는 반환 받은 스케일의 중간값 반환
    xyzScale = []
    temp = [1, 2]

    for i in temp:  # pCube의 좌표값을 번호대호 반환 반복
        p = cmds.getAttr("Scale" + str(i) + ".scale")  # 좌표값이 튜플로 입력됨
        print(p)
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


def ReturnFinalRnaVal(xyzRangeList, targetcount):
    uniDBs = []  # xyz값을 순서대로 오브젝트상 적용 가능하게 통합

    x = count_gen(xyzRangeList[0][0], xyzRangeList[0][1], targetcount)
    y = count_gen(xyzRangeList[1][0], xyzRangeList[1][1], targetcount)
    z = count_gen(xyzRangeList[2][0], xyzRangeList[2][1], targetcount)

    for i in range(targetcount):
        uniDBs.append([x[0], y[0], z[0]])  # 좌표값 리스트 0번 인덱스 오브젝트 인덱스 0번으로 입력
        x.pop(0)  # 입력한 인덱스 값 삭제 추후 pop값 로그로 출력모듈 도입
        y.pop(0)
        z.pop(0)

    return uniDBs  # 랜덤 사이즈값 반환


def mainFucScl(temp):
    a = GetVecVal()  # 오브젝트 스케일값 입력후 반환
    b = xyzRange(a)  # 입력받은 스케일 좌표값 x,y,z 범위로 정렬
    c = ReturnFinalRnaVal(b, temp)

    return c  # 랜덤하게 반환된 좌표값 반환

