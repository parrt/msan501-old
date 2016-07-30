# a linked list implementation using 2-element lists like tuples
# adds/removes to the head of the list like a stack. Also has
# insertafter
import string

head = None
VALUE = 0
NEXT = 1


def add(x):
    global head
    head = [x, head]


def deletefirst():
    global head
    if head is None:
        return
    head = head[NEXT]  # point to what was next head.next


def show():
    values = []
    p = head
    while p is not None:
        values.append(p[VALUE])
        p = p[NEXT]
    print str(values)


def contains(x):
    p = head
    while p is not None:
        if x == p[VALUE]:
            return True
        p = p[NEXT]
    return False


def index(x):
    i = 0
    p = head
    while p is not None:
        if x == p[VALUE]:
            return i
        i += 1
        p = p[NEXT]
    return -1


def getitem(j):
    "get ith node in the list starting from 0"
    i = 0
    p = head
    while p is not None:
        if i == j:
            return p
        i += 1
        p = p[NEXT]
    return None


def insertafter(i, x):  # add x after ith node
    p = getitem(i)
    if p is not None:
        p[NEXT] = [x, p[NEXT]]


def len():
    'student exercise'


add("parrt")
add("tombu")
add("afedosov")

show()

print "index('parrt') =", index('parrt')
print "index('tombu') =", index('tombu')
print "index('afedosov') =", index('afedosov')
print "index('foo') =", index('foo')

print "getitem(0) =", getitem(0)
print "getitem(1) =", getitem(1)
print "getitem(2) =", getitem(2)

deletefirst()
deletefirst()
show()

print contains("parrt")
print contains("foo")

insertafter(0, "jimbo")
show()
