#!/usr/bin/env python3
"""Define the function"""


from pymongo import MongoClient


def nginx_log_stats():
    """
    Connects to the MongoDB logs database
    assesses the nginx collection and prints statistics
    about the logs.
    """
    client = MongoClient('localhost', 27017)

    db = client.logs
    nginx_collection = db.nginx

    total_logs = ngonx_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_checks = nginx_collection.
    count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")


if __name__ == "__main__":
    nginx_log_stats()
