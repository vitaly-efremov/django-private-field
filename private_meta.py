class PrivateFieldsMeta(models.base.ModelBase):
    """
    Meta class that looks at **private_fields** attribute in Model Meta Option
    and renames the class attribute to **_{attribute}**, but keeps db column name original.

    This allows to encapsulate field's data.

    Short example here.

    >>> class Employee(models.Model, metaclass=PrivateFieldsMeta):
    >>>     name = models.CharField(max_length=256)
    >>>     rate = models.FloatField(default=0)
    >>>
    >>>     class Meta:
    >>>         private_fields = ('rate', )
    >>>
    >>>
    >>> Employee(name='John', rate=15)
    >>> TypeError: 'rate' is an invalid keyword argument for this function
    >>>
    >>> employee = Employee(name='John')
    >>> employee.rate
    >>>
    >>> AttributeError: 'Employee' object has no attribute 'rate'
    >>> employee._rate
    >>>
    >>> 0
    >>> Employee.objects.filter(rate=12)
    """
    def __new__(cls, name, bases, attrs):
        attr_meta = attrs.pop('Meta', None)

        private_fields = getattr(attr_meta, 'private_fields', ())
        for private_field_name in private_fields:
            field = attrs.pop(private_field_name, None)
            if field:
                field.db_column = private_field_name
                attrs['_%s' % private_field_name] = field

        result = super(PrivateFieldsMeta, cls).__new__(cls, name, bases, attrs)
        return result
