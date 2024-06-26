class Subject:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

class Observer:
    def update(self, temperature):
        raise NotImplementedError

class TemperatureDisplay(Observer):
    def update(self, temperature):
        print(f'Temperature Display: New temperature is {temperature}°C')

class TemperatureLogger(Observer):
    def update(self, temperature):
        print(f'Temperature Logger: Logging new temperature {temperature}°C')

if __name__ == "__main__":
    # Criar o subject
    temperature_sensor = Subject()
    
    # Criar observers
    display = TemperatureDisplay()
    logger = TemperatureLogger()
    
    # Registrar os observers
    temperature_sensor.register_observer(display)
    temperature_sensor.register_observer(logger)
    
    # Alterar temperatura e notificar observers
    temperature_sensor.set_temperature(25)
    temperature_sensor.set_temperature(30)
