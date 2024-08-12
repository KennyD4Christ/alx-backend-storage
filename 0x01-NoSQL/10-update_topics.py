#!/usr/bin/env python3
""" 10-update_topics """

from pymongo.collection import Collection
from typing import List


def update_topics(mongo_collection: Collection, name: str,
                  topics: List[str]) -> None:
    """ Update the topics field for all documents with the specified name.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        name (str): The name of the school document(s) to update.
        topics (List[str]): The list of topics to set in the topics field.
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    print(result.raw_result)  # Print raw result for debugging
