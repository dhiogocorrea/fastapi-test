import importlib
from db import MyDatabase
import threading
import uuid
from models import NF


mydb = MyDatabase()

def submit_nf(state, data):
    nf_id = str(uuid.uuid4())

    t = threading.Thread(target=crawl_data, args=(nf_id, state, data))
    t.start()

    return nf_id

def crawl_data(nf_id, state, data):
    mod = importlib.import_module("crawlers." + state)
    result = mod.crawl(data)
    mydb.save(result)


def get_nf(nf_id):
    response = mydb.get(nf_id)
    return NF().from_response(response)


def delete_nf(nf_id):
    mydb.delete(nf_id)