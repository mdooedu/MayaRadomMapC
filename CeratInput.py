import maya.cmds as cmds
from MadedFucRe import *


a = int(input("값을 입력받을 큐브의 갯수\n"))
temp = int(input("만들 좌표의 갯수\n"))


def CreatRelocate(ranlocin, ransclin, temp):
    RanLocDB = ranlocin
    RanSclDB = ransclin

    for i in range(1, temp+1):

        temp += 1
        iNam = str(i)
        nam = "pSphere"
        tran = nam + iNam + '.translate'
        rot = nam + iNam + '.rotate'
        sca = nam + iNam + '.scale'
        x_01 = RanLocDB.pop([0][0])
        y_01 = RanLocDB.pop([0][0])
        z_01 = RanLocDB.pop([0][0])
        x_02 = RanSclDB.pop([0][0])
        y_02 = RanSclDB.pop([0][0])
        z_02 = RanSclDB.pop([0][0])
        print(x_01, y_01, z_01)
        cmds.duplicate(nam + iNam)
        cmds.setAttr(tran, x_01, y_01, z_01)
        cmds.setAttr(sca, x_02, y_02, z_02)

    return


'''
이름 입력값 에러 확인
이전 함수 정상 구현
29번 행렬에서 에러확인 
# Error: RuntimeError: file <maya console> line 157: setAttr: Error reading data element number 1: [3.3085998401400776, -3.29712531343791, 0.7952717226266673]
'''


print(mainFucScl(temp))  # 랜덤 반환된 사이즈값