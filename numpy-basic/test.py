import numpy

#One dimensional array
a = numpy.arange(25)
print(" One dimensional array")
print(a)

#Two dimensional array
b = a.reshape(5,5)
print("\n Two dimensional array")
print(b)

#Three dimensional array
c = numpy.arange(27)
c = c.reshape(3,3,3)
print("\n Three dimensional array")
print(c)

#convert list into numpy array
x= [[1,2,3,4],[2,3,5],[]]
# print(type(x))
d = numpy.asarray([[1,2,3,4],[2,3,5],[]])
print("\n Convert list into numpy array")
print(d)
print(type(d))