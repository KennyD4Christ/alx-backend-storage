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

if __name__ == "__main__":
    # Example code for testing purposes
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
