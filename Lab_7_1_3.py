# import Lab_7_1_1  # якщо повністю файл. то перед класом треба вказати файл Lab_7_1_1.BuildingMaterials
from Lab_7_1_1 import BuildingMaterials

def test_plus(value, expected):   #задали 
    test_obj = BuildingMaterials('brick', 'yellow', 200)
    number_before = test_obj.number  # подивилисяб що було до
    test_obj.plus(value)             #виконали операцію +
    number_after = test_obj.number   #що сталося після 
    assert value == (number_after-number_before)
    print('test successfull')

     
def main():
    brick = BuildingMaterials('brick', 'yellow', 200)
    plank = BuildingMaterials('plank', 'red', 10)
    
    brick.info()
    plank.info()
    
    brick.plus(1)
    plank.minus(2)
    
    brick.info()
    plank.info()
    
if __name__ == "__main__":
    print("__", __name__)
    main()
    
    
    test_plus(10)
    
    


