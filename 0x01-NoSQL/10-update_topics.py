#!/usr/bin/env python3
"""Define the function"""


def update_topics(mongo_collection, name, topics):
    """
    Insert a new document in a collection based on kwargs

    Args:
      mongo_collection: Pymongi collection object.
      name (string): The school name to update.
      topics (list): List of topics approached in the school.

    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    }
