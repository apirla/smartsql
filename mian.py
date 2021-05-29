from smartsql import F, T, QS, Condition
from datetime import datetime

def select_list(start_time=None, end_time=None, uid=None):
    sql = QS(T.user).where({
        'start_time': {
            "$gt": start_time
        },
        'end_time': {
            "$lt": end_time
        },
        'uid': uid
    }).select()
    return sql


if __name__ == '__main__':
    print(select_list(start_time=datetime.now(), uid=[1, 23, 53, 11]))