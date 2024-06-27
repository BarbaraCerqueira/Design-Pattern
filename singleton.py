class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = open('app.log', 'a')
        return cls._instance

    def log(self, message):
        self._instance.log_file.write(message + '\n')

    def __del__(self):
        self._instance.log_file.close()

# Uso do Singleton
logger1 = Logger()
logger2 = Logger()

logger1.log("Mensagem de log 1")
logger2.log("Mensagem de log 2")

print(logger1 is logger2)  # Saída: True, confirmando que ambas as variáveis apontam para a mesma instância
