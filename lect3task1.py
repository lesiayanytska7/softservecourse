'''знайти в заданій стрічці кільуість входжень'''
string = "Beautiful is better than ugly.\
Explicit is better than implicit.\
Simple is better than complex.\
Complex is better than complicated. \
Flat is better than nested. \
Sparse is better than dense. \
Readability counts. \
Special cases aren't special enough to break the rules. \
Although practicality beats purity. \
Errors should never pass silently. \
Unless explicitly silenced. \
In the face of ambiguity, refuse the temptation to guess. \
There should be one-- and preferably only one --obvious way to do it. \
Although that way may not be obvious at first unless you're Dutch. \
Now is better than never. \
Although never is often better than *right* now. \
If the implementation is hard to explain, it's a bad idea. \
If the implementation is easy to explain, it may be a good idea. \
Namespaces are one honking great idea -- let's do more of those"
substring1 = 'better'
substring2 = 'never'
substring3 = 'is'
count1 = string.count(substring1)
print('count of better is:', count1)
count2 = string.count(substring2)
print('count of never is:', count2)
count3 = string.count(substring3)
print('count of better is:', count3)

'''вивести весь текст у верхньому регістрі'''
print(string.upper())

'''замінити всі входження символу і на &'''
print(string.replace('i', '&'))