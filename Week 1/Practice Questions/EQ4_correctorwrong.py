#  Correct word or partially correct or wrong word

d={
    "their":"their",
    "business":"bisiness",
    "windows":"wimdmill",
    "were":"wear",
    "sample":"sample",
    "sipu":"lipu"
    }
 
def find_correct(d):
    c = 0
    ac = 0
    w = 0
    for i, j in d.items():
        if len(i) == len(j):
            flag = 0
            for k in range(0, len(i)):
                if i[k] != j[k]:
                    flag = flag + 1
            if flag == 0:
                c = c + 1
            elif flag <= 2:
                ac = ac + 1
            else:
                w = w + 1
        else:
            w = w + 1
    return list((c, ac, w))

print(find_correct(d))
