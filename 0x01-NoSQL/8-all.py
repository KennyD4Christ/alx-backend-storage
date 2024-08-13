#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.

    Returns:
        list: A list of documents in the collection, or an empty list if none found.
    """
    documents = list(mongo_collection.find())
    return documents if documents else []
