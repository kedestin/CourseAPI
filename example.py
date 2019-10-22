import tufts_courses as tufts
import json

"""
Pretty print
"""


def pprint(obj):
    print(json.dumps(obj, indent=2))


def main():
    career = tufts.getCareer()[0]
    term = tufts.getTerms(career=career["value"])[0]
    subject = tufts.getSubjects(
        career=career["value"], term=term["value"])
    toFind = subject[10]
    print("Results for search with parameters: ")
    pprint({"career": career["value"],
            "term": term["value"], "subject": toFind["desc"]})

    pprint(tufts.performSearch(
        career=career["value"], term=term["value"], subject=toFind["value"])[0])


if __name__ == "__main__":
    main()
