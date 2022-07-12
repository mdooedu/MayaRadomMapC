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
        xyzScale.append(cmds.getAttr("Scale" + str(i) + ".scale"))

    return xyzScale


print(GetVecVal())
