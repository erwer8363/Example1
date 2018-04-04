from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print('{} and {}'.format(p.x,p.y))