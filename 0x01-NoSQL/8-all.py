#!/usr/bin/env python3
"""Define the function"""


def list_all(mongo_collection):
    """
    lists all documents in a collection

    Args:
      mongo_collection: Pymongi collection object
    """
    return mongo_collection.find()
