#!/usr/bin/env python3
"""Module for retrieving schools by topic from a MongoDB collection."""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of dictionaries representing the schools that have the
        specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
