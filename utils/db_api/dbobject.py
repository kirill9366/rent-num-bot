class DBObject:
    """English: The class represents a record object

    ...

    Attributes
    ----------
    peewee_obj : class
        Peewee class

    Methods
    -------
    get_field(name_field)

    """

    def __init__(self, peewee_obj):
        self.peewee_obj = peewee_obj

    def get_field(self, name_field):
        """Get value of field record

        Parameters
        ----------
        name_field : str
            The name of the field whose value you want to

        """
        return getattr(self.peewee_obj, name_field)

    async def update_field(self, name_field, new_value):
        """Updates the object data

        Parameters
        ----------
        name_field : str
            The name of the field whose value you want to
        new_value : str, int
            New field value

        """
        setattr(self.peewee_obj, name_field, new_value)
        self.peewee_obj.save()

    async def delete(self):
        """Delete record"""
        self.peewee_obj.delete_instance()
