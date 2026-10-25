#-*- coding: cp1251 -*-

class HistoricalFigure:
    def __init__(self, name, age_1, age_2, text):
        self.name = name
        self._age_1 = age_1
        self.age_2 = age_2
        self.text = text
        print(f"Исторический персонаж {self.name} записан.")
    
    def __str__(self):
        return (f"ФИО: {self.name}\n"
                f"Годы жизни: {self._age_1} - {self.age_2}\n"
                f"Чем известин: {self.text}")
    
    def __del__(self):
        print(f"Исторический персонаж  {self.name} удалён.")

    @property
    def age_1(self):
        return self._age_1
        
    @staticmethod    
    def get_text():
        return HistoricalFigure.text
    def __calculate_age(self):
        return self.age_2 - self._age_1

    def get_age_at_death(self):
        age = self.__calculate_age()  
        return f"{self.name} жил до {self.age_2} и прожил {age} лет."

    def read_attribute(self, attribute_name):
        return getattr(self, attribute_name, "Атрибут не найден")

    def delete_attribute(self, attribute_name):
        if hasattr(self, attribute_name):
            delattr(self, attribute_name)
            return f"Атрибут '{attribute_name}' удалён"
        else:
            return f"Атрибут '{attribute_name}' не существует"
    

num_i = int(input("Сколько надо ввести исторических персонажей: "))
users = []
for i in range(0,num_i):
    if __name__ == "__main__":
        name = input("Фамилия И.О.:  ")
        age_1 = int(input("Дата рождения:  "))
        age_2 = int(input("Дата смерти:   "))
        text = input("Чем известин:  ")
        users.append(HistoricalFigure(name, age_1, age_2, text)) 

print('------')

for i in range(0,num_i):
    print(users[i])
    print(users[i].get_age_at_death())
    print("Год раждения: ")
    print(users[i].age_1)
    print(' ')
    print(users[i].read_attribute('text'))
    print(users[i].delete_attribute('text'))
    print(users[i].read_attribute('text'))
    print(' ')
    
del users
