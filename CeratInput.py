import maya.cmds as cmds
from MadedFucRe import *


a = int(input("값을 입력받을 큐브의 갯수\n"))
temp = int(input("만들 좌표의 갯수\n"))


def creatReturnLocation(a, temp):
    reBDtoin = []

    reBDtoin.append(mainFucLoc(a, temp))  # 랜덤 로케이션 반환값

    for i in range(temp):

        temp += 1
        iNam = str(i)
        nam = "pSphere1"
        tran = nam + iNam + '.translate'
        rot = nam + iNam + '.rotate'
        sca = nam + iNam + '.scale'
        x_01 = reBDtoin.pop([0][0])
        y_01 = reBDtoin.pop([0][0])
        z_01 = reBDtoin.pop([0][0])
        x_02 = reBDtoin.pop([0][0])
        y_02 = reBDtoin.pop([0][0])
        z_02 = reBDtoin.pop([0][0])
        x_03 = reBDtoin.pop([0][0])
        y_03 = reBDtoin.pop([0][0])
        z_03 = reBDtoin.pop([0][0])
        print(x_01, y_01, z_01)
        cmds.duplicate(nam)
        cmds.setAttr(tran, x_01, y_01, z_01)
        cmds.setAttr(sca, x_02, y_02, z_02)
        cmds.setAttr(rot, x_03, y_03, z_03)

    return


print(mainFucScl(temp))  # 랜덤 반환된 사이즈값