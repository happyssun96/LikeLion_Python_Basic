#1번
List1 = [[[1, 2], [3]], [4], [5, [6, 7]]]
n = List1[0][0][1]
q = List1[-1][0]
print(n,q)

#2번
str = "010-1234-1234"
print(str.replace("-", "*"))

'''
a = list('010-1234-1234')
mid = (len(a)//2)
a[mid] = '*'
b = "".join(a)
print(b)
'''
#3번
List2 = [{'name': 'Anthony Edward Stark', 'age': 53, 'nickname': 'IronMan'},
     {'name': 'Thor', 'age': 1500, 'nickname': 'God of Thunder'},
     {'name': 'Natasha Romanoff', 'age': 39, 'nickname': 'Black Widow'}]
print(List2[0]['name'])

"""
value1 = {
    'name': 'Anthony Edward Stark',
    'age': 53,
    'nickname': 'IronMan'
}
value2 = {
    'name': 'Thor',
    'age': 1500,
    'nickname': 'God of Thunder'
}
value3 = {
    'name': 'Natasha Romanoff',
    'age': 39,
    'nickname': 'Black Widow'
}
print(value1['nickname'])
"""