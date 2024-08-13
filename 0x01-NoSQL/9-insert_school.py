#!/usr/bin/env python3

"""
Module for Listing all documents in a collection
"""

from typing import List, Dict
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict]:
    """ List all documents in a collection.

    Args:
        mongo_collection (Collection): The pymongo collection object.

    Returns:
        List[Dict]: A list of all documents in the collection.
    """
    return list(mongo_collection.find())


if __name__ == "__main__":
