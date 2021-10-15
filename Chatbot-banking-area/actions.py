from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from elasticsearch import Elasticsearch
from rasa_core_sdk.events import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests as rq

import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host
                     user="root",  # username
                     passwd="",  # password
                     db="bank")  # name of the database

def get_tokens(text, analyzer="custom_analyzer"):
    host = ''
    response = rq.get(host, json={"analyzer": analyzer, "text": text})
    return list(map(lambda x: x['token'], response.json()['tokens']))


def tokens_to_term(weighted_tokens):
    prepared_tokens = []
    for token, value in weighted_tokens.items():
        prepared_token = {
            "term": {
                "text": {
                    "value": token,
                    "boost": value
                }
            }
        }
        prepared_tokens.append(prepared_token)
    return prepared_tokens


def search_by_tokens(tokens, query=None, index="sections_defs"):
    host = ''
    if query:
        body = query
    else:
        body = {
            "query": {
                "bool": {
                    "must": tokens
                }
            }
        }

    url = host + index + "/_search"
    response = rq.post(url, json=body)

    return response.json()


def get_keywords(text):
    custom_stopwords = ['A', '.', 'I', 'me', 'my', 'your', 'we']
    stop_words = stopwords.words('english') + custom_stopwords
    words = word_tokenize(text)
    keywords = [w for w in words if w not in stop_words]
    return keywords


class ActionSearchElastic(Action):

    def name(self):
        return "give_definitions_of_types_of_accounts"

    def run(self, dispatcher, tracker, domain):
        w_tokens = {}
        last_message = tracker.latest_message['text']
        for token in get_tokens(last_message):
            w_tokens[token] = 1
        prep_tokens = tokens_to_term(w_tokens)
        res = search_by_tokens(prep_tokens)
        msgs = res['hits']['hits'][0]['_source']['text']
        dispatcher.utter_message('If you are confused we can help you with additional info about types of accounts:'
                                 + msgs)


class ActionBlokCustomer(Action):
    def name(self):
        return 'action_blok_customer'

    def run(self, dispatcher, tracker, domain):
        try:
            c = db.cursor()

            no_rek = tracker.get_slot('norek')

            c.execute("SELECT * FROM customer WHERE no_rek =" + no_rek + "")

            result = c.fetchone()

            ibu_kandung = result[1]
            nama = result[2]
            tipe_rek = result[3]
            alamat = result[4]

            response = """Nama ibu kandung saudara adalah {}. \nPemilik ATM yang bernama {}. \nTipe rekening {}. \nYang beralamat di {}. \nUntuk keamanan bersama, maka ATM saudara kami blokir untuk eementara\n""".format(ibu_kandung, nama, tipe_rek, alamat)
            dispatcher.utter_message(response)

        except:
            response = """Masukkan kembali nomor rekening saudara"""
            dispatcher.utter_message(response)
            return [SlotSet("norek", no_rek)  ]

class ActionPinCustomer(Action):
    def name(self):
        return 'action_pin_customer'

    def run(self, dispatcher, tracker, domain):
        try:
            c = db.cursor()

            no_rek = tracker.get_slot('norek')

            c.execute("SELECT * FROM custpin WHERE no_rek =" + no_rek + "")

            result = c.fetchone()

            pin_atm = result[1]

            response = """Pin ATM saudara adalah {}\n""".format(pin_atm)
            dispatcher.utter_message(response)

        except:
            response = """Masukkan kembali nomor rekening saudara"""
            dispatcher.utter_message(response)
            return [SlotSet("norek", no_rek)]

class ActionSaldoCustomer(Action):
    def name(self):
        return 'action_saldo_customer'

    def run(self, dispatcher, tracker, domain):
        try:
            c = db.cursor()

            no_rek = tracker.get_slot('norek')

            c.execute("SELECT * FROM custsaldo WHERE no_rek =" + no_rek + "")

            result = c.fetchone()

            saldo = result[1]

            response = """Jumlah Saldo Rekening saudara adalah Rp {},00\n""".format(saldo)
            dispatcher.utter_message(response)

        except:
            response = """Masukkan kembali nomor rekening saudara"""
            dispatcher.utter_message(response)
            return [SlotSet("norek", no_rek)]