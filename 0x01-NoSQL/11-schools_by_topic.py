#!/usr/bin/env python3
""" 11-schools_by_topic """

from typing import List, Dict
from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict]:
    """
    Returns a list of schools with a specific topic.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List[Dict]: List of dictionaries representing the schools with
        the specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))
