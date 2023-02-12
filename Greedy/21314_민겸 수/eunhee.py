string = input()


def change_m_num(string):
    return 10**(string.count("M")-1)


def min_num(string):    # M이 최대한 긴거를 뽑아내기.
    res = ""
    str_combi = ""
    for s in string:
        if s == "K":
            num = ""
            if str_combi:
                num = str(change_m_num(str_combi))
            res += num+"5"
            str_combi = ""
        else:
            str_combi += s
    if str_combi:
        res += str(change_m_num(str_combi))
    return res


def max_num(string):    # 끝에 K가 붙어있는 최대 긴 M 뽑아내기
    res = ""
    str_combi = ""
    for s in string:
        if s == "K":
            num = "5"
            if str_combi:
                num = str((10**str_combi.count("M"))*5)
            res += str(num)
            str_combi = ""
        else:
            str_combi += s
    if str_combi:
        res += "1"*str_combi.count("M")
    return res


print(max_num(string))
print(min_num(string))
