# """
# #   TITLE   :
# #   DATE    :
# #   USER    :
# #   NOTE    :
# """

"""
#   TITLE   :
#   DATE    :
#   USER    :
#   NOTE    :
"""

class commFunc():

    # 공통 클래스 초기화
    def __init__(self):
        pass



class B:
    """
    # TITLE : GETTER / SETTER 내장 함수 사용 예제

    """
    def __init__(self, name):
        self.name = name
        self.id = name+" HIHI"
        print("self.name :: ", self.name)

    def __getattr__(self, name):
        print(" __getattr__")

        setattr(self, name, "default")

        return self.__dict__[name]


## GETTER / SETTER 내장 함수 사용 예제
b = B("dahl")
print(b.name)
print("getattr name :: ", getattr(b, "name"))
print("getattr id :: ", getattr(b, "id"))