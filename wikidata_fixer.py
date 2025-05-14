from random import shuffle

import requests



def get_wikidata_label(entity_id, language="en"):
    url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbgetentities",
        "ids": entity_id,
        "format": "json",
        "languages": language,
        "props": "labels",
    }
    response = requests.get(url, params=params)
    data = response.json()
    try:
        return data["entities"][entity_id]["labels"][language]["value"]
    except KeyError:
        return None


def translate_line(line: str):
    triple = line.strip().split("\t")
    subject_label = triple[0]
    predicate_label = triple[1]
    if "longtiude" in predicate_label:
        predicate_label = predicate_label.replace("longtiude", "longitude")
    object_label = triple[2]

    return subject_label + "\t" + predicate_label + "\t" + object_label + "\n"

triples = []
with open("../KGs/LitWD1K/numeric_literals_translated5.txt", "r") as f:
    for line in f:
        triples.append(line)

d = int(len(triples)/10)

shuffle(triples)
a = triples
# with open("../KGs/LitWD1K/numerical_literals_train.txt", "w") as f:
with open("../KGs/LitWD1K/numerical_literals_test.txt", "w") as f2:
    for i in range(d):
        f2.write(a[i])
        triples.pop(i)

with open("../KGs/LitWD1K/numerical_literals_train.txt", "w") as f1:
    for line in triples:
        f1.write(line)

# print(translate_line("namibia	inflation_rate_1	0.073"))