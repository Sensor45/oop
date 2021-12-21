# from functools import redude
# print(reduce(lambda acc, x: acc+x,  ['H', 'e', 'l','l','o']))
# -----------------------------------------------------------------------------
# print(list(map(lambda x: int(x),['2', '4', '3','10'])))
# -------------------------------------------------------------------------------
# from random import randint
# from functools import reduce
#
# nums = [randint(1, 100) for _ in range(10)]
# print(nums)
#
# print(reduce(lambda acc, a: acc+a, (filter(lambda x: x % 2 == 0, nums))))
# -------------------------------------------------------------------------------

text = 'london is the capital, london very very bid city'

def get_word_count(text_,word_):
    list_text = text.split(' ')


print(text)