#!/usr/bin/env python3
"""
Module for retrieving students sorted by average score from a MongoDB
collection.
"""


def top_students(mongo_collection):
    """
    Returns a list of all students sorted by their average score.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of dictionaries where each dictionary represents a student with
        their average score.
    """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
