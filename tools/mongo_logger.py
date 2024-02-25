import streamlit as st
import os
import argparse
import dataclasses
from datetime import datetime
from pymongo import MongoClient

@dataclasses.dataclass
class MongoConfig:
    uri: str = None
    db_name: str = None
    collection_name: str = None
    client: MongoClient = dataclasses.field(init=False, default=None)
    db: MongoClient = dataclasses.field(init=False, default=None)
    collection: MongoClient = dataclasses.field(init=False, default=None)
    connection_status: bool = dataclasses.field(init=False, default=False)

    def __post_init__(self):
        self.uri = self.uri or st.secrets["mongodb"]["uri"] if "mongodb" in st.secrets else os.environ.get('MONGO_URI', '')
        self.db_name = self.db_name or st.secrets["mongodb"]["db"] if "mongodb" in st.secrets else os.environ.get('MONGO_DB', '')
        self.collection_name = self.collection_name or st.secrets["mongodb"]["collection"] if "mongodb" in st.secrets else os.environ.get('MONGO_COLLECTION', '')
        self.connect()
    
    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
            self.connection_status = True
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            self.connection_status = False
        
    def write_log(self, values):
        if not self.connection_status:
            return
        if not isinstance(values, dict):
            print("Invalid input to log. Expected dictionary.")
            return
        values["timestamp"] = datetime.now()
        try:
            self.collection.insert_one(values)
            print("Log successfully written to MongoDB.")
        except Exception as e:
            print(f"Failed to write log to MongoDB: {e}\n{values}")
    
    def get_records(self, filter=None):
        if not self.connection_status:
            return []
        filter = filter or {}  # Use an empty dict if filter is None
        try:
            records = list(self.collection.find(filter))
            for record in records:
                record['_id'] = str(record['_id'])  # Convert ObjectId to string
            return records
        except Exception as e:
            print(f"Failed to retrieve records from MongoDB: {e}")
            return []
        
    def get_by_tag(self, tag):
        return self.get_records({"tag": tag})

    def report_by_tag(self, tag):
        records = self.get_by_tag(tag)
        for record in records:
            print(record)
        print(f"Retrieved {len(records)} records from MongoDB with tag '{tag}'.")

    def report_all(self):
        records = self.get_records()
        for record in records:
            print(record)
        print(f"Retrieved all {len(records):,} records from MongoDB.")

mongo_db = MongoConfig()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Log generated text to MongoDB.')
    parser.add_argument('-f', '--feedback', action='store_true', help='Show feedback logged MongoDB.')
    parser.add_argument('-c', '--cards', action='store_true', help='Show cards logged to MongoDB.')    
    parser.add_argument('-l', '--log', type=str, help='Log the generated text to MongoDB.')
    parser.add_argument('-r', '--retrieve', action='store_true', help='Retrieve all records from MongoDB.')
    args = parser.parse_args()

    if args.log:
        mongo_db.write_log({"text": args.log, "tag": "test"})
        print(f"Logged '{args.log}' to MongoDB.")

    if args.retrieve:
        # get all records from the MongoDB
        mongo_db.report_all()

    if args.feedback:
        # get all records that have a value of tag = feedback
        mongo_db.report_by_tag("feedback")

    if args.cards:
        # get all records that have a value of tag = generated_text
        mongo_db.report_by_tag("generated_text")
