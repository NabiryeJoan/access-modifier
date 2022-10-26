class Person:
    def __init__(self,name,age,country):
 
        self.name =name 
        self.age = age
        self.country = country
        # getter
    @property
    def country (self):
        return self.__country
    #  setter
    @country.setter
    def country (self,value):
        if(value not in ['uganda','kenya','cong']):
            raise('country not in east africa')
        self.__country = value
        
        
        
    def __str__(self):
        return f'Name is {self.name} and age is {self.age} and country is {self.country}'
    # updating the data
person1 = Person("john Doe",16,'uganda')
person1.name = 'jim'
person1.age = 12
person1.country= 'canada'



print(person1)
    
        