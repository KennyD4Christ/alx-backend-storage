#!/usr/bin/env python3
"""Module for updating topics of a school document in a MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    
    Args:
        mongo_collection: The pymongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics to be set for the school.
    
    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
