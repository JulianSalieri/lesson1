def get_summ(one, two, delimiter='&'):
    get_sam_one = (str(one + delimiter + two))
    # print(get_sam_one.upper())
    return get_sam_one


#one1 = 'Learn'
#two2 = 'python'
# get_summ(one1, two2)

result = get_summ('Learn', 'python')
print(result.upper())
