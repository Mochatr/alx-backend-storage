#!/usr/bin/env python3
"""Define the function"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic

    Args:
      mongo_collection: Pymongi collection object.
      topics (string): Topic searched.

    Returns:
      List of school having a specific topic.

    """
    return mongo_collection.find({"topics": topic})
