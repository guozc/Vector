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

print("---------------------------------------------")

v11 = Vector([-7.579,-7.88])
v12 = Vector([22.737,23.64])

v21 = Vector([-2.029,9.97,4.172])
v22 = Vector([-9.231,-6.639,-7.245])

v31 = Vector([-2.328,-7.284,-1.214])
v32 = Vector([-1.821,1.072,-2.94])

v41 = Vector([2.118,4.827])
v42 = Vector([0,0])

print(v11.is_parallel_with(v12))
print(v11.is_orthogonal_with(v12))

print(v21.is_parallel_with(v22))
print(v21.is_orthogonal_with(v22))

print(v31.is_parallel_with(v32))
print(v31.is_orthogonal_with(v32))

print(v41.is_parallel_with(v42))
print(v41.is_orthogonal_with(v42))

print("---------------------------------------------")
print(math.cos(1))
print(math.cos(math.pi-1))