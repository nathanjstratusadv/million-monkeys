from peewee import CharField


class EnumField(CharField):
    def __init__(self, enum_class, *args, **kwargs):
        self.enum_class = enum_class
        # Convert enum to choices format
        choices = [(member.value, member.name.title()) for member in enum_class]
        super().__init__(choices=choices, *args, **kwargs)

    def python_value(self, value):
        # Convert database value back to enum
        if value is None:
            return None
        try:
            return self.enum_class(value)
        except ValueError:
            return value  # Return original if not found

    def db_value(self, value):
        # Convert enum to database value
        if isinstance(value, self.enum_class):
            return value.value
        return value