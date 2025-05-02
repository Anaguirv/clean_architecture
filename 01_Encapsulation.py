class Circle:
    
    def __init__(self, radio: float):
        self.radio = radio

    def __get_pi(self):
        return 3.1416
    
    def area(self):
        return self.__get_pi() * self.radio ** 2
    
if __name__ == '__main__':
    circle = Circle(10)
    print(circle.area())

    import ipdb
    ipdb.set_trace()
    print(circle._Circle__get_pi()) # Para invocar un método "privado" debemos invocar a la clase 