knightHP, knightATK, witchHP, witchATK = map(int, input().split())
witchSkill, IncreaseHP = map(int, input().split())
HPflag = False

while True:
    witchHP -= knightATK

    if (witchHP <= 0):
        print('Victory!')
        break

    knightHP -= witchATK

    if (knightHP <= 0):
        print('gg')
        break

    if (1 <= witchHP <= witchSkill and HPflag == False):
        witchHP += IncreaseHP
        HPflag = True