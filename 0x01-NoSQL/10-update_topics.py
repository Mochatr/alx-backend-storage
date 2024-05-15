#!/usr/bin/env python3
"""Define the function"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name.

    Args:
      mongo_collection: Pymongi collection object.
      name (string): The school name to update.
      topics (list): List of topics approached in the school.

    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    }
