class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of_rect(self):
        return self.width * self.height

    def perimetr_of_rect(self):
        return (self.width + self.height) * 2


rect_1 = Rect(2, 4)
rect_2 = Rect(5, 3)
rect_3 = Rect(3.6, 4)

print('Периметр первого -', rect_1.perimetr_of_rect())
print('Периметр второго -', rect_2.perimetr_of_rect())
print('Периметр третьего -', rect_3.perimetr_of_rect())
print('\n')
print('Площадь первого', rect_1.area_of_rect())
print('Площадь второго', rect_2.area_of_rect())
print('Площадь третьего', rect_3.area_of_rect())
print('\n')


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print('Сложение -', result)

    def multiplication(self):
        result = self.a * self.b
        print('Умножение -', result)

    def division(self):
        result = self.a / self.b
        print('Деление -', result)

    def subtraction(self):
        result = self.a - self.b
        print('Вычитание -', result)


num = Math(3, 4)
num.addition()
num.multiplication()
num.division()
num.subtraction()
print('\n')


class Site:
    def __init__(self, text, element='Кнопка', loc=None):
        self.text = text
        self.element = element
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)


button_1 = Site('Text Box')
print(button_1.click())

button_2 = Site('Check Box')
print(button_2.click())
button_3 = Site('Radio Button')
print(button_3.click())
button_4 = Site('Web Tables')
print(button_4.click())
button_5 = Site('Buttons')
print(button_5.click())
button_6 = Site('Links')
print(button_6.click())
button_7 = Site('Broken Links - Images')
print(button_7.click())
button_8 = Site('Upload and Download')
print(button_8.click())
button_9 = Site('Dynamic Properties')
print(button_9.click())
