class node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
    


def inOrder(r):
    if r:
        inOrder(r.left)
        print(r.data,end = ' ')
        inOrder(r.right)
def add(r,data):
    if not r:
        return node(data)
    else:
        if data < r.data:
            r.left = add(r.left, data)
        else:
            r.right = add(r.right, data)
        return r
def printSideWay(r,level):
    if r:
        printSideWay(r.right,level + 1)
        print(' '*3*level,r.data)
        printSideWay(r.left,level + 1)
def height(r):
    if not r:
        return -1
    else:
        hl = height(r.left)
        hr = height(r.right)
        if hl>hr:
            return hl+1
        else:
            return hr+1
def path(r, d):
    if r.data != d:
        print(r.data,end = '')
        if d < r.data:
            path(r.left, d)
        else:
            path(r.right, d)
    else:
        print(d)
def search(r, d):
    if not r:
        return None
    if r.data == d:
        return r
    else:
        if d < r.data:
            return search(r.left, d)
        else:
            return search(r.right, d)
def depth(r, d):
    if not r:
        return -1
    if r.data == d:
        return 0
    else:
        if d < r.data:
            return depth(r.left, d) + 1
        else:
            return depth(r.right, d) + 1

l = [14, 4, 9, 7, 15, 3, 18, 16, 20, 5, 16]
print('input: ', l)

r = None
for ele in l:
    r = add(r,ele)

print('inorder: ', end=' ')
inOrder(r)
print()

print('printSideWay: ')
printSideWay(r, 0)

print('height of ', r.data, '=', height(r))

d = 5
print('path:', d, '=', end=' ')
path(r, d)

d = 9
t = search(r, d)
print(t.data)

d = 18
print('depth of node data ', d, '=', depth(r, d))