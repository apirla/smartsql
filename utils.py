from smartsql import ConditionSet, F


def list2cond(li):
    conds = ConditionSet()
    for cond in li:
        conds &= cond
    return conds
if __name__ == '__main__':
    print(list2cond([F.asdasda > 1212]).sql)


