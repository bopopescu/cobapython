# d={}
# for x in range(1,10):
#     d["string{0}".format(x)]="Hello"
#     print(d)

for x in range(0, 9):
    globals()['string%s' % x] = 'Hello'
    vars = globals()['string%s' % x]
    print(vars)