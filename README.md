Introduction
------------
Small Django Model extension which make particular fields private and encapsulate field's data.

PrivateFieldsMeta metaclass that looks at **private_fields** attribute in Model Meta Option and renames the class attribute to **_{attribute}**, but keeps db column name original.

How to use
------------    
Short example here.
```
class Employee(models.Model, metaclass=PrivateFieldsMeta):
    name = models.CharField(max_length=256)
    rate = models.FloatField(default=0)
    
    class Meta:
        private_fields = ('rate', )

>>> Employee(name='John', rate=15)
>>> TypeError: 'rate' is an invalid keyword argument for this function

>>> employee = Employee(name='John')
>>> employee.rate
>>> AttributeError: 'Employee' object has no attribute 'rate'

>>> employee._rate
>>> 0

>>> Employee.objects.filter(rate=12)
```
