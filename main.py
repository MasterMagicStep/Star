def params( a=11, b='Hell`s', c = False):
    print(a,b,c)
#
print(params())
print(params(b="UnDefeating"))
print(params(c=[2,5,7]))
print('---------------')
#
ValueList = (11 , "Hell`s",True)
params(*ValueList)
ValueDict = {'a':13, 'b': "Hellish", 'c': False}
params(**ValueDict)
print('--------------')
#
ValueList2 = [59.60, 'Automata']
params(*ValueList2,47)