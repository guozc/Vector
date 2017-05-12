import math

"""向量类"""
class Vector(object):
    MSG_ZERO_ERR = "The direction of zero vector cannot be determined!"

    """初始化，填入坐标"""
    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = [float(x) for x in coordinates] #分量值
            self.dimension = len(coordinates) #维度

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError(self.MSG_ZERO_ERR)

    def __str__(self):
        return 'Vector:{}'.format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self,other):
        new_coordinates = [x+y for x,y in zip(self.coordinates,other.coordinates)]
        return Vector(new_coordinates)

    def __sub__(self,other):
        new_coordinates = [x-y for x,y in zip(self.coordinates,other.coordinates)]
        return Vector(new_coordinates)

    """判断是否为零向量"""
    def is_zero(self):
        return self.magnitude() < 1e-10

    """乘以数值"""
    def scalar(self,scalar):
        new_coordinates = [scalar*x for x in self.coordinates]
        return Vector(new_coordinates)

    """返回向量的长度"""
    def magnitude(self):
        return math.sqrt(sum([x**2 for x in self.coordinates]))

    """返回单位向量,0向量无法确定单位向量"""
    def direction(self):
        try:
            return Vector([x/self.magnitude() for x in self.coordinates])

        except ZeroDivisionError:
            raise Exception("The direction of zero vector cannot be determined!")

    """点乘"""
    def dot(self,other):
        new_coordinates = [x*y for x,y in zip(self.coordinates,other.coordinates)]
        return sum(new_coordinates)

    """两个向量之间的夹角，0向量除外"""
    def with_angle(self,other,show_in_degress = False):
        try:
            n1_direction = self.direction()
            n2_direction = other.direction()
            angle = math.acos(n1_direction.dot(n2_direction))

            if show_in_degress:
                per_degress_in_radian = 180./math.pi
                return angle*per_degress_in_radian
            else:
                return angle

        except Exception as e:
            if str(e) == self.MSG_ZERO_ERR:
                raise Exception("The angle between the zero vector and the other vector cannot be calculated! ")
            else:
                raise e

    """判断两个向量平行是否平行"""
    def is_parallel_with(self,other):
        if self.is_zero() or other.is_zero():
            return True
        elif self.with_angle(other) == 0 or self.with_angle(other) == math.pi:
            return True
        else:
            return False

    """两个向量是否正交"""
    def is_orthogonal_with(self,other):
        return abs(self.dot(other))<1e-10

