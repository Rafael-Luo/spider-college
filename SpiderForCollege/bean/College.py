"""
大学类
name:高校名
city:高校所在城市
department:高校归属哪个部门管理
levels:高校层次
url:高校官网

"""


class College(object):

    def __init__(self, name='', icon='', city='', type='', department='', levels='', character='', url='', score=''):
        self._name = name
        self._icon = icon
        self._city = city
        self._type = type
        self._department = department
        self._levels = levels
        self._character = character
        self._url = url
        self._score = score

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, new_cion):
        self._icon = new_cion

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        self._city = new_city

    @property
    def type(self):
        return self._type

    @city.setter
    def type(self, new_type):
        self._type = new_type

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department):
        self._department = new_department

    @property
    def levels(self):
        return self._levels

    @levels.setter
    def levels(self, new_levels):
        self._levels = new_levels

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, new_character):
        self._character = new_character

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, new_url):
        self._url = new_url

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score


    def toString(self):
        # (college.name, college.city, college.type, college.department, college.levels, college.character, college.score)
        return '院校名称:'+college.name+'院校所在地:'+college.city+'院校隶属:'+college.department+'院校类型:'+college.type+'学历层次:'+college.levels+'院校特性:'+college.character+'满意度:'+college.score+''


if __name__ == '__main__':
    college = College()
    college.url = "aaa"
    college.city = 'aaa'
    college.url = 'bbb'
    college.character='aaa'
    college.score='aaa'
    college.levels='aaa'
    college.department='aaa'
    college.name='ds'

    print(college.toString())
