class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            self._successor.handle(request)

class BasicSupport(Handler):
    def handle(self, request):
        if request == "basic":
            print("BasicSupport: Resolvendo pedido básico.")
        else:
            print("BasicSupport: Passando para o próximo nível.")
            super().handle(request)

class AdvancedSupport(Handler):
    def handle(self, request):
        if request == "advanced":
            print("AdvancedSupport: Resolvendo pedido avançado.")
        else:
            print("AdvancedSupport: Passando para o próximo nível.")
            super().handle(request)

class SpecialistSupport(Handler):
    def handle(self, request):
        if request == "specialist":
            print("SpecialistSupport: Resolvendo pedido especializado.")
        else:
            print("SpecialistSupport: Nenhum handler disponível para esse pedido.")

if __name__ == "__main__":
    # Configuração da cadeia de responsabilidade
    specialist_support = SpecialistSupport()
    advanced_support = AdvancedSupport(specialist_support)
    basic_support = BasicSupport(advanced_support)

    # Cliente fazendo pedidos
    print("Cliente solicita suporte básico.")
    basic_support.handle("basic")

    print("\nCliente solicita suporte avançado.")
    basic_support.handle("advanced")

    print("\nCliente solicita suporte especializado.")
    basic_support.handle("specialist")

    print("\nCliente solicita suporte não definido.")
    basic_support.handle("undefined")
