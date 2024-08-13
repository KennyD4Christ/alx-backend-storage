#!/usr/bin/env python3
""" 9-insert_school """

from pymongo import MongoClient
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


if __name__ == "__main__":
    # Example code for testing purposes
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    new_school_id = insert_school(school_collection, name="New School",
                                  location="123 Main St", founded=2024)
    print(f"Inserted school with _id: {new_school_id}")
