'''добуток цифр числа'''
num = int(input('Input your 4-digits number: '))
mult = 1
while (num !=0):
    mult = mult * (num % 10)
    num = num // 10
    print('Result is: ', mult)

'''записати число в реверсному порядку'''
#first approach
num = int(input('Input your 4-digits number: '))
reverse = 0
while (num>0):
    reminder = num %10
    reverse = (reverse *10) + reminder
    num = num //10
print('\n reverse of innputed number is = %d' %reverse)

#second approach
num=str(input('Input your 4-digits number: '))
print("Reverse of the given number is: ")
print(num[::-1])


'''посортувати цифри'''
num = input('Input your 4-digits number for sort: ')
sort_num = sorted(num)
print(sort_num)
