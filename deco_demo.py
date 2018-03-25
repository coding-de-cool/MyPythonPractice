# Decorators in Python

class Harley:

    def __init__(self, **kwargs):
        self.features = kwargs

    def setter(self, k, v):
        self.features[k] = v

    def getter(self, k):
        return self.features.get(k, None)

    def seat(self):
        super().seat()
        print('Seat of Harley is awesome')

    @property
    def top_speed(self):
        return self.features.get('top_speed', None)

    @top_speed.setter
    def top_speed(self, ts):
        self.features['top_speed'] = ts

    @top_speed.deleter
    def top_speed(self):
        del self.features['top_speed']


street_bob = Harley()
street_bob.setter('cc', '1800')
print(street_bob.getter('cc'))
street_bob.setter('color', 'Black')
print('The color of bike is', street_bob.getter('color'))
street_bob.top_speed = 1000