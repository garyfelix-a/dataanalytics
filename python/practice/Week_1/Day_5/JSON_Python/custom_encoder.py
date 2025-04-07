import json

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class StudentEncoder(json.JSONEncoder):
    # overrides default() method
    def default(self, obj):
        # isinstace(obj, Student) checks if the object is of class Student
        if isinstance(obj, Student):
            # if yes, then it returns the dictionary of data
            return {
                'name': obj.name,
                'age': obj.age
            }
        # if not, use the default encoder.
        return super().default(obj)
    
std =  Student("Randy", 32)
json_data = json.dumps(std, cls=StudentEncoder)
print(json_data)