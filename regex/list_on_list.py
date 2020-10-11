# bq = "INSERT INTO table_name (user_id, post) VALUES "
# for i in range(10):
#     bq += "(1, 'test'),"
# bq = bq.strip(',') + ';'
# print(bq) 


# def listmerge(lst:list) -> list:
#     res = []
#     for el in lst:
#         res += listmerge(el) if isinstance(el, list) else [el]
#     return res
# t = [1,[2],2,2,[2,3,6],[4,[5,6],6],7] # 12
bg = [7,[[[[2]]],[[[]],[4]],[4,5,[6,7]]],8] # 8
# tb =[[1,2], [3,4], [5,6,7], [8]] # 8
# print(listmerge(t), len(listmerge(t)))
# print(listmerge(bg), len(listmerge(bg)))
# print(listmerge(tb), len(listmerge(tb)))

import re
def lst(l:list) -> list:
    return list(map(int, re.findall("[1-9]", str(l))))

print(lst(bg))
