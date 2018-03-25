from inherit import Bike


class Harley(Bike):

    def __init__(self, **kwargs):
        self.features = kwargs

    def setter(self, k, v):
        self.features[k] = v

    def getter(self, k):
        return self.features.get(k, None)

    def seat(self):
        super().seat()
        print('Seat of Harley is awesome')


street_bob = Harley()
street_bob.seat()
street_bob.setter('cc', '1800')
print(street_bob.getter('cc'))
street_bob.setter('color', 'Black')
print('The color of bike is', street_bob.getter('color'))
