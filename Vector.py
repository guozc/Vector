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

    """一个向量在另一个向量上的投影,即一个向量在另一个向量上的平行分量"""
    def projection_component(self,other):
        try:
            magnitude = self.dot(other)/other.magnitude()
            return other.direction().scalar(magnitude)
        except Exception as e:
            if str(e) == self.MSG_ZERO_ERR:
                raise Exception("Zero vectors do not have unique parallel vectors")

    """一个向量在另一个向量上的垂直分量"""
    def orthogonal_component(self,other):
        try:
            projection = self.projection_component(other)
            return self - projection
        except Exception as e :
            if str(e) == self.MSG_ZERO_ERR:
                raise Exception("Zero vectors do not have unique vertical vectors")

    """将1、2维向量转成3维向量"""
    def to_vector3(self):
        zero_vector3 = Vector([0.,0.,0.])
        new_vector3 = zero_vector3+self
        if new_vector3.dimension<3:
            for i in range(0,3-new_vector3.dimension%3):
                new_vector3 = Vector(new_vector3.coordinates+[0.])
        return new_vector3


    """叉乘，3维向量有几何意义"""
    def cross(self,other):
        ax,ay,az = self.to_vector3().coordinates
        bx,by,bz = other.to_vector3().coordinates

        return Vector([ay*bz-az*by,-(ax*bz-az*bx),ax*by-ay*bx])

    """组成平面的面积"""
    def area_cross(self,other):
        return self.cross(other).magnitude()