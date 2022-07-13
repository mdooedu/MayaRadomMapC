import maya.cmds as cmds
from MadedFucRe import *


a = int(input("값을 입력받을 큐브의 갯수\n"))
temp = int(input("temp\n"))

print(mainFucLoc(a, temp))  # 랜덤 로케이션 반환값
print(mainFucScl(temp))  # 랜덤 반환된 사이즈값
'''
정상출력 확인 mainFucLoc, mainFucScl
'''
