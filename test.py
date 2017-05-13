from Vector import Vector
import math

v1 = Vector([1,2,3])
v2 = Vector([1,2,3])
v3 = Vector([2,3,4])
zero =Vector([0,0,0])
v4 = Vector([0,1])
v5 = Vector([0,-1])

print(v1)
print(v1==v2)

print(v1+v2)
print(v1-v2)
print(v1.scalar(3))


print(v1.magnitude()) #长度
print(v1.direction()) #单位向量

print(v1.direction().magnitude()) #验证单位向量长度为1

print(v1.dot(v1))
print(v1.with_angle(v1))

print(v4.is_parallel_with(zero))

print(v4.projection_component(v5))
print(v1.projection_component(v1))


print(v1.cross(v1))
print(v2.area_cross(v3))

