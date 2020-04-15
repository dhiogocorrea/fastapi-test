import importlib
from db import MyDatabase
import threading
import uuid
from models import NF


mydb = MyDatabase()

def submit_nf(state, data):
    data['status'] = 'Processando'

    nf_id = mydb.save(data)

    t = threading.Thread(target=crawl_data, args=(nf_id, state, data))
    t.start()

    return nf_id

def crawl_data(nf_id, state, data):
    mod = importlib.import_module("crawlers." + state.lower())
    data = mod.crawl(data)

    data['status'] = 'Concluido'

    mydb.update(nf_id, data)


def get_nf(nf_id):
    return mydb.get(nf_id)


def delete_nf(nf_id):
    mydb.delete(nf_id)