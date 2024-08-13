#!/usr/bin/env python3
""" 9-insert_school """

from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """ Insert a new document into a collection.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        **kwargs: Arbitrary keyword arguments representing the document fields.

    Returns:
        str: The _id of the new document.
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
