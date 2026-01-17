from abc import ABC, abstractmethod


class Shape(ABC):
    """Базовый класс для самих фигур"""
    
    def __init__(self):
        """Инициалицация класса фигур"""
        super().__init__()
        self.coordinates = [0, 0]
        self.color = "white"
    
    
    @abstractmethod
    def execute(self, shape, task, *args):
        """Абстрактный метод для выполнения задачи"""
        pass
    

    def draw(self):
        """Не понял для чего использовать"""
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
            *args (Разные типы): Несколько параметров в зависимости от задачи
        """
        if task == 'AddShape':
            canvas.shapes.append([shape])
            self.history.append([shape, task])
        if task == 'RemoveShape':
            canvas.shapes.remove([shape])
        if task == 'MoveShape':
            shape.old_coordinates = shape.coordinates
            shape.coordinates = args[0]
        if task == 'ChangeColor':
            shape.old_color = shape.color
            shape.color = args[0]
            self.history.append([shape, task])
    
    def info(self):
        print(f'Круг: {self.coordinates}. Цвет: {self.color}')
    
    def __str__(self):
        return f'Круг {self.color}'
    
   
class EditorCommand(Shape):
    """ Класс для обработки команд """
    
    def __init__(self):
        """ Инициализация обработчика команд """
        self.history = []
    
    
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
            self.history.append([shape, task])
        if task == 'RemoveShape':
            canvas.shapes.remove([shape])
        if task == 'MoveShape':
            shape.old_coordinates = shape.coordinates
            shape.coordinates = args[0]
        if task == 'ChangeColor':
            shape.old_color = shape.color
            shape.color = args[0]
            self.history.append([shape, task])
            
            
    def undo(self, shape:Shape):
        """Метод для отмены изменений цвета"""
        shape.color = shape.old_color
        print(f"Отменено") 
  
    
class EditorHistory():
    """Класс для хранения истории изменений"""
    history = [] 
    

class ChangeColor(Shape):
    """Класс для опреации смены цвета"""
    
    def __init__(self, new_color: str):
        """Инициализация"""
        super().__init__()
        self.color = new_color
        self.old_color = None

    def execute(self, shape:Shape):
        """
        Метод для выполнения задачи
        
        Params:
            shape (Shape): Экземпляр фигуры
        
        Return:
            Сообщение о выполнении
        """
        self.old_color = shape.color
        shape.color = self.new_color
        print(f"Цвет изменён")

    def undo(self, shape:Shape):
        shape.color = self.old_color
        print(f"Отменено") 

   
canvas = Canvas()
        
circle = Circle([10, 10], 'green')
edit = EditorCommand()
edit.execute(canvas, circle, 'AddShape')
print(f'new color {circle.color}')
print(f'old color {circle.old_color}')
print(canvas.shapes)
#edit.execute(canvas, circle, 'RemoveShape')


print(circle.color) # Смена цвета
edit.execute(canvas, circle, 'ChangeColor', 'red')
print(circle.color)

print(circle.coordinates)
edit.execute(canvas, circle, 'MoveShape', [100, 100])
print(circle.coordinates)

print(circle)
edit.undo(circle)
