"""
public, protected, private
_ private/protected (public _)
__ private (_classname__attributename)
"""


class DataBase:
    def __init__(self):
        self.__data = {}

    @property
    def data(self):
        return self.__data

    def insert_customer(self, id, name):
        if 'customers' not in self.__data:
            self.__data['customers'] = {id: name}
        else:
            self.__data['customers'].update({id: name})

    def show_customers(self):
        for id, name in self.__data['customers'].items():
            print(id, name)

    def delete_customer(self, id):
        del self.__data['customers'][id]


bd = DataBase()
bd.insert_customer(1, 'misa')
bd.insert_customer(2, 'lucy')
bd.insert_customer(3, 'megumin')
print(bd.data)
# bd.show_customers()
