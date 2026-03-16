import datetime

versions = {}

def save_version(doc_id, text):

    if doc_id not in versions:
        versions[doc_id] = []

    versions[doc_id].append({
        "time": datetime.datetime.now(),
        "text": text
    })