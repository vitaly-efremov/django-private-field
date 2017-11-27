from django.db import models
from private_field_meta import PrivateFieldsMeta


class Employee(models.Model, metaclass=PrivateFieldsMeta):
    name = models.CharField(max_length=256)
    rate = models.FloatField(default=0)

    class Meta:
        private_fields = ('rate',)

    def __repr__(self):
        return '%s(%s$)' % (self.name, self._rate)

    def set_rate(self, value):
        self._rate = value * 3


if __name__ == '__main__':
    employee = Employee(name='John')
    employee.set_rate(11)
    employee.save()

    print(Employee.objects.filter(rate__gte=10))
