#!/usr/bin/env python3
""" 102-log_stats.py """

from pymongo import MongoClient


def log_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.
    - Number of logs
    - Breakdown of log methods
    - Number of logs with status check
    - Top 10 most present IPs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total number of logs
    log_count = nginx_collection.count_documents({})
    print(f"{log_count} logs")

    # Method statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Number of logs with status check
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")

    # Top 10 most present IPs
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = nginx_collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
