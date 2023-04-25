class Animal:
    def __init__(self, patas):
        self.patas = patas

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{key}={value}" for key, value in self.__dict__.items()])}'


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)


class Gato(Mamifero):
    pass


# class Ornitorrinco(Mamifero, Ave):
#     pass

class FalarMixin:
    def falar(self):
        return 'Ola, estou falando'


class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, patas):

        # print(Ornitorrinco.__mro__)   -> Ordem da resuloção para encontrar os atributos e métodos
        # print(Ornitorrinco.mro())     -> Ordem da resuloção para encontrar os atributos e métodos

        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, patas=patas)


gato = Gato(patas=4, cor_pelo='branco')
print(gato)

ornitorrinco = Ornitorrinco(patas=4, cor_pelo='marrom', cor_bico='preto')
print(ornitorrinco)
print(ornitorrinco.falar())
