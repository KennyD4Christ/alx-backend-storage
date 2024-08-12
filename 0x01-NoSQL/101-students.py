#!/usr/bin/env python3
""" 101-students """

from typing import List, Dict
from pymongo.collection import Collection


def top_students(mongo_collection: Collection) -> List[Dict]:
    """
    Returns a list of all students sorted by average score.

    Args:
        mongo_collection (Collection): The pymongo collection object for
        students.

    Returns:
        List[Dict]: A list of students with their averageScore, sorted by
        averageScore.
    """
    # Aggregation pipeline
    pipeline = [
        {
            "$project": {
                "name": 1,
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

    # Execute aggregation pipeline
    results = list(mongo_collection.aggregate(pipeline))

    return results
