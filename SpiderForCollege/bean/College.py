"""
大学类
name:高校名
city:高校所在城市
department:高校归属哪个部门管理
levels:高校层次
url:高校官网

"""


class College(object):

    def __init__(self, name='', city='', type='', department='', levels='', url=''):
        self._name = name
        self._city = city
        self._type = type
        self._department = department
        self._levels = levels
        self._url = url

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

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
    def url(self):
        return self._url

    @url.setter
    def url(self, new_url):
        self._url = new_url


if __name__ == '__main__':
    college = College
    college.url = "aaa"
    college.city = 'aaa'
    college.url = 'bbb'
    print(college.url + college.city)
