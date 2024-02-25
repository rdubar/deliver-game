# mongo_logger.py
import streamlit as st
import os
import argparse
from datetime import datetime
from pymongo import MongoClient
import ast
import json
from datetime import datetime
import dateutil.parser

"""
Manage logging of generated text to MongoDB.
"""

# Setup MongoDB connection
try:
    mongo_uri = st.secrets["mongodb"]["uri"] if "mongodb" in st.secrets else os.environ.get('MONGO_URI', '')
    client = MongoClient(mongo_uri)
    db_name = st.secrets["mongodb"]["db"] if "mongodb" in st.secrets else os.environ.get('MONGO_DB', '')
    collection_name = st.secrets["mongodb"]["collection"] if "mongodb" in st.secrets else os.environ.get('MONGO_COLLECTION', '')
    db = client[db_name]
    collection = db[collection_name]
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    mongo_uri = None

if not mongo_uri:
    print("MongoDB URI not found. Please setup in secrets.toml.")

def log_mongo(values):
    """
    Logs dictionary of values to MongoDB.
    """
    if not mongo_uri:
        return
    if not isinstance(values, dict):
        print("Invalid input to log_text. Expected dictionary.")
        return
    values["timestamp"] = datetime.now()
    try:
        collection.insert_one(values)
        print("Log successfully written to MongoDB.")
    except Exception as e:
        print(f"Failed to write log to MongoDB: {e}\n{values}")

def get_all_records():
    """
    Retrieves all records from the MongoDB collection.

    Returns:
    - A list of dictionaries, each representing a document in the collection.
    """
    try:
        records = list(collection.find({}))
        # Optionally, convert ObjectId to string or perform other formatting
        for record in records:
            record['_id'] = str(record['_id'])  # Convert ObjectId to string for easier handling
        return records
    except Exception as e:
        print(f"Failed to retrieve records from MongoDB: {e}")
        return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Log generated text to MongoDB.')
    parser.add_argument('-f', '--feedback', action='store_true', help='Show feedback logged MongoDB.')
    parser.add_argument('-c', '--cards', action='store_true', help='Show cards logged to MongoDB.')    
    parser.add_argument('-l', '--log', type=str, help='Log the generated text to MongoDB.')
    parser.add_argument('-r', '--retrieve', action='store_true', help='Retrieve all records from MongoDB.')
    args = parser.parse_args()

    # if args.log:
    #     log_mongo(args.log)
    if args.retrieve:
        records = get_all_records()
        print(f"Retrieved {len(records)} records from MongoDB.")
        for record in records:
            print(record)

    if args.feedback:
        records = collection.find({"feedback": {"$exists": True}})
        print(f"Retrieved {records.count()} feedback records from MongoDB.")
        for record in records:
            print(record)

    if args.cards:
        records = collection.find({"generated_text": {"$exists": True}})
        print(f"Retrieved {records.count()} generated text records from MongoDB.")
        for record in records:
            print(record)
