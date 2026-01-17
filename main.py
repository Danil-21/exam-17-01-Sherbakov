from abc import ABC, abstractmethod


#------------------------------
#Докстринги писать


# Базовый класс для самих фигур
class Shape(ABC):
    
    def __init__(self):
        super().__init__()
        self.coordinates = [0, 0]
        self.color = "white"
    
    
    @abstractmethod
    def execute(self, shape, task):
        # Абстрактный метод для выполнения задачи
        pass
    
    # Здесь можно сделать добавление на холст
    def draw(self):
        pass
    

class Canvas():
    """
    Класс для создания холста
    """
    available_shapes = [
        'Circle',
        'Rectangle',
        'Line'
    ]
    shapes = []
    
    
shape_id = 0


# Класс для круга
class Circle(Shape):
    """Класс для объекта: Круг"""
    
    def __init__(self, coordinates, color):
        """
        Метод для инициализации круга
        
        Params:
            coordinates (List): Координаты фигуры
            color (Str): Цвет фигуры
        """
        super().__init__()
        self.coordinates = coordinates
        self.old_coordinates = [0, 0]
        self.color = color
        self.old_color = None
        global shape_id
        self.id = shape_id + 1
        shape_id += 1    
    
    
    def execute(self, canvas: Canvas, shape: Shape, task, *args):
        """
        Метод для выполнения задачи
        
        Params:
            canvas (Canvas): Экземпляр холста
            shape (Shape): Экземпляр фигуры
            task (Str): Задача, которую нужно выполнить
        """
        if task == 'AddShape':
            canvas.shapes.append([shape])
            print(1)
        pass
    
    def info(self):
        print(f'Круг: {self.coordinates}. Цвет: {self.color}')
    
    def __str__(self):
        return self.info()
    

class ChangeColor():
    pass

   
class EditorCommand(Shape):
    """ Класс для обработки команд """
    
    def __init__(self):
        """ Инициализация обработчика команд """
        super().__init__()
    
    
    def execute(self, canvas: Canvas, shape: Shape, task, *args):
        """
        Метод для выполнения задачи
        
        Params:
            canvas (Canvas): Экземпляр холста
            shape (Shape): Экземпляр фигуры
            task (Str): Задача, которую нужно выполнить
            *args (Разные типы): Несколько параметров в зависимости от задачи
        """
        if task == 'AddShape':
            canvas.shapes.append([shape])
        if task == 'RemoveShape':
            canvas.shapes.remove([shape])
        if task == 'MoveShape':
            shape.old_coordinates = shape.coordinates
            shape.coordinates = args[0]
        if task == 'ChangeColor':
            shape.old_color = shape.color
            shape.color = args[0]

    
class EditorHistory():
    history = [] 
    
    
canvas = Canvas()
        
circle = Circle([10, 10], 'green')
edit = EditorCommand()
edit.execute(canvas, circle, 'AddShape')
print(f'new color {circle.color}')
print(f'old color {circle.old_color}')
print(canvas.shapes)
#edit.execute(canvas, circle, 'RemoveShape')


# print(circle.color) # Смена цвета
# edit.execute(canvas, circle, 'ChangeColor', 'red')
# print(circle.color)

print(circle.coordinates)
edit.execute(canvas, circle, 'MoveShape', [100, 100])
print(circle.coordinates)

#print(canvas.shapes[0].color)
# circle.execute()
