import src.tufts_courses as tufts
import json


def pprint(obj):
    """
    Pretty print
    """
    print(json.dumps(obj, indent=2))


def main():
    career = tufts.getCareer()[0]
    term = tufts.getTerms(career=career["value"])[0]
    subject = tufts.getSubjects(career=career["value"], term=term["value"])
    toFind = subject[10]

    print("Performing search")
    pprint(
        {
            "career": career["value"],
            "term": term["value"],
            "subject": toFind["desc"]
        }
    )

    print("\nFirst result:")
    pprint(
        tufts.performSearch(
            career=career["value"],
            term=term["value"],
            subject=toFind["value"]
        )["searchResults"][0]
    )


if __name__ == "__main__":
    main()
