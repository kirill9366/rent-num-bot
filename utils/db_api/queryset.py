from .dbobject import DBObject


class QuerySet:
    """Interacts with the database
    ...

    Attributes
    ----------
    model : peewee_object
        peewee model class

    Methods
    -------
    get_object(**kwargs)
        Get a DBObject object with the passed attributes

    select_objects(where=None, order_by=None)
        Select a object with the passed attributes

    """

    def __init__(self, model, objects):
        self.model = model
        self.objects = objects

    async def _get_condition(self, where):
        field = getattr(self.model, where['field'])
        if where['operator'] == '==':
            return field == where['value']
        elif where['operator'] == '!=':
            return field != where['value']
        elif where['operator'] == '<':
            return field < where['value']
        elif where['operator'] == '>':
            return field > where['value']
        elif where['operator'] == '<=':
            return field <= where['value']
        elif where['operator'] == '>=':
            return field >= where['value']

    async def get_object(self, **kwargs):
        """Get a DBObject object with the passed attributes

        Parameters
        ----------
        **kwargs
            Parameters for getting a object

        """
        peewee_object = await self.objects.get(
            self.model,
            **kwargs,
        )
        return DBObject(peewee_object)

    async def select_objects(self, where=None, order_by=None):
        """Select a object with the passed attributes

        Parameters
        ----------
        where : dict, optional
            A dictionary with the following fields:
                field : str
                    Name of the object field
                operator : str
                    String representation of an operator
                    Examples: ==, !=, <, >, <=, >=
                value : str, int, DBObject
                    The value to be compared with.
        order_by : str
            The name of the field to be sorted by

        """

        if where:
            where = await self._get_condition(where)

        peewee_objects = await self.objects.execute(
            self
            .model
            .select()
            .where(where)
            .order_by(order_by)
        )
        return list(map(DBObject, peewee_objects))

    async def create_object(self, **kwargs):
        """Creates an record in the database

        Parameters
        ----------
        **kwargs
            Field names and their values

        """
        peewee_object = await self.objects.create(
            self.model,
            **kwargs,
        )
        return DBObject(peewee_object)
