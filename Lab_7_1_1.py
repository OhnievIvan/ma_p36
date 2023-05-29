print('this is my class', __name__)

class BuildingMaterials:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number
        self.place(number)
        
    def place(self, n):
        if n <= 0:
            print('out of stock')
        elif 0 < n < 100:
            print('werehouse')
        else:
            print('Remote House')
            
    def plus(self, count):
        self.number += count
        self.place(self.number)
    
    def minus(self):
        self.number -= count
        self.place(self.number)
        
            
    def info(self):
        print(f"material: {self.material}, color: {self.color}, number: {self.number}")
        
if __name__ == "__main__":
    mat1 = BuildingMaterials('wood', 'brown', 20)
    # mat1.place(mat1.number)
    mat2 = BuildingMaterials('stone', 'grey', 10)
    
    mat1.info()
    mat2.info()
    
    brick = BuildingMaterials('brick', 'white', 300)
    plank = BuildingMaterials('plank', 'brown', 20)
    
    # print(brick.material, brick.color, brick,number)
    brick.info()
    plank.info()
    
    brick.plus(50)
    plank.minus(3)
    