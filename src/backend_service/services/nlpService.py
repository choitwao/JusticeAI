import requests

NLP_URL = "http://0.0.0.0:3002"


def tenant_landlord(message):
    req_dict = {
        "answer": message
    }
    res = requests.post("{}/{}".format(NLP_URL, "tenant_landlord"), json=req_dict)
    return res.json()


def problem_category(message):
    req_dict = {
        "answer": message
    }
    res = requests.post("{}/{}".format(NLP_URL, "problem_category"), json=req_dict)
    return res.json()


def fact_extract(facts, message):
    req_dict = {
        "answer": message,
        "facts": facts
    }
    res = requests.post("{}/{}".format(NLP_URL, "fact_extract"), json=req_dict)
    return res.json()
