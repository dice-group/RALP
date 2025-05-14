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
    subject_id = triple[0]
    predicate_id = triple[1].split("_")[0]
    if len(triple[1].split("_")) > 1:
        predicate_quantity_label = triple[1].split("_")[1]
    else:
        predicate_quantity_label = ""
    object = triple[2]
    subject_label = get_wikidata_label(subject_id)
    if subject_label is None:
        subject_label = get_wikidata_label(subject_id, "de")
        if subject_label is None:
            print(f"Skipped: {line}")
            return
    subject_label = subject_label.lower().replace(" ", "_")
    predicate_label = get_wikidata_label(predicate_id).lower().replace(" ", "_")
    # predicate_quantity_label = get_wikidata_label(predicate_quantity_id).lower().replace(" ", "_")
    # object_label = re.search(r'"[\+\-]?([0-9]+\.[0-9]+)"', object).group(1)
    if "dateTime" in object:
        object_label = object.split('"')[1]
    else:
        object_label = str(float(object.split('"')[1]))

    return subject_label + "\t" + predicate_label + "_" + predicate_quantity_label + "\t" + object_label + "\n"

with open("../KGs/LitWD1K/numeric_literals2.txt", "r") as f:
    with open("../KGs/LitWD1K/numeric_literals_translated.txt", "a") as f2:
        for line in f:
            f2.write(translate_line(line))