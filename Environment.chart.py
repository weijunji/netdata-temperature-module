from bases.FrameworkServices.SimpleService import SimpleService
from w1thermsensor import W1ThermSensor

update_every = 5
retries = 5

ORDER = ['Temperature']

CHARTS = {
    'Temperature': {
        'options': [None, 'Temperature', 'Temperature', 'Temperature', 'environment.temp', 'line'],
        'lines': [
            ["Temperature", None, 'absolute', 1, 100]
        ]
    }
}

class Service(SimpleService):
    def __init__(self, configuration=None, name=None):
        SimpleService.__init__(self, configuration=configuration, name=name)
        self.order = ORDER
        self.definitions = CHARTS
        self.sensor = W1ThermSensor()

    def _get_data(self):
        try:
            temp = self.sensor.get_temperature()
            if(temp > -50 and temp < 80):
                return {'Temperature': temp * 100}
            else:
                return None
        except ValueError:
            return None

    @staticmethod
    def check():
        return True
