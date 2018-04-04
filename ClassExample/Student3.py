class Student3(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 10000:
            raise ValueError('score must between 0~100')
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth


s = Student3()
s.birth = 2010
print(s.birth)
print(s.age)