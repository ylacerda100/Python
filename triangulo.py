class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        p = self.a + self.b + self.c
        return p


    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c:
            return 'isósceles'
        else:
            return 'escaleno'

    
    def retangulo(self):
        lados = [self.a, self.b, self.c]
        maior = max(lados)
        for i in lados:
            if i == maior:
                lados.remove(i)
                break
        if maior**2 == (lados[0]**2 + lados[1]**2):
            return True
        else:
            return False


    def semelhantes(self, Triangulo):
        lista_a = [self.a, self.b, self.c]
        lista_b = [Triangulo.a, Triangulo.b, Triangulo.c]
        s = lista_a[0]/lista_b[0]
        for i in range(3):
            if lista_a[i]/lista_b[i] == s:
                semelhantes = True
            else:
                semelhantes = False
        return semelhantes