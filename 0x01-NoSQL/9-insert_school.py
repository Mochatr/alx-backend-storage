#!/usr/bin/env python3
"""Define the function"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs

    Args:
      mongo_collection: Pymongi collection object

    Returns:
      The new _id.
    """
    inserted_object = mongo_collection.insert_one(kwargs)

    return inserted_object.inserted_id
