class Cafe:
    def preco(self):
        return 5.0

class DecoratorCafe:
    def __init__(self, cafe):
        self._cafe = cafe
    
    def preco(self):
        return self._cafe.preco()

class Leite(DecoratorCafe):
    def preco(self):
        return self._cafe.preco() + 1.5

class Acucar(DecoratorCafe):
    def preco(self):
        return self._cafe.preco() + 0.5

if __name__ == "__main__":
    meu_cafe = Cafe()
    print("Preço do café simples:", meu_cafe.preco())

    meu_cafe_com_leite = Leite(meu_cafe)
    print("Preço do café com leite:", meu_cafe_com_leite.preco())

    meu_cafe_com_leite_acucar = Acucar(meu_cafe_com_leite)
    print("Preço do café com leite e açúcar:", meu_cafe_com_leite_acucar.preco())
