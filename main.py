#!/usr/bin/python3
import src.tufts_courses
import tufts_degree_sheet
import json

    # "ACL-0013", Prise Seminar
courses_taken = [
    "CHEM-0001",
    "COMP-0011",
    "COMP-0015",
    "COMP-0040",
    "COMP-0061",
    "COMP-0111",
    "COMP-0122",
    "COMP-0160",
    "EE-0014",
    "EE-0021",
    "EE-0023",
    "EE-0024",
    "EE-0026",
    "EE-0031",
    "EN-0001",
    "ENG-0001",
    "ES-0002",
    "ES-0003",
    "ES-0004",
    "FAM-0064",
    "MATH-0032",
    "MATH-0034",
    "MATH-0042",
    "MATH-0070",
    "MUS-0009",
    "PHY-0011",
    "PHY-0012"
]

def pretty_print(obj):
    print(json.dumps(obj, indent=2))


def main():
    for c, course in reversed(list(enumerate(courses_taken))):
        for val, section in reversed(list(enumerate(tufts_degree_sheet.CE_2022))):
            # print(section,val)
            for counter, requirement in reversed(list(enumerate(tufts_degree_sheet.CE_2022[section]["courses"]))):
                for counter2, classs in reversed(list(enumerate(requirement))):
                    if classs == course:
                        del tufts_degree_sheet.CE_2022[section]["courses"][counter]
                        if section == "concentration":
                            # print(cours)
                            del courses_taken[c]
        
    # pretty_print(courses_taken)
    pretty_print(tufts_degree_sheet.CE_2022)
    for c, course in reversed(list(enumerate(courses_taken))):
        for val, section in reversed(list(enumerate(tufts_degree_sheet.CS_2022))):
            # print(section,val)
            
            for counter, requirement in reversed(list(enumerate(tufts_degree_sheet.CS_2022[section]["courses"]))):
                for counter2, classs in reversed(list(enumerate(requirement))):
                    if classs == course:
                        # print(course)
                        del tufts_degree_sheet.CS_2022[section]["courses"][counter]
                        if section == "concentration":
                            # print(c)
                            del courses_taken[c]
    pretty_print(tufts_degree_sheet.CS_2022)
    # pretty_print(courses_taken)
    # pretty_print(tufts_degree_sheet.CE_2022)
    # for course in courses_taken:
        # sub_no = course.split("-")
        # pretty_print(tufts_courses.performSearch(2192, subject=sub_no[0], crs_number=sub_no[1]))
    # pretty_print(tufts_courses.getCareer())
    # pretty_print(tufts_courses.getSubjects(2195, "ALL"))
    # pretty_print(tufts_courses.getAttributes(2195, "ALL"))
    # pretty_print(tufts_courses.getCourseNumbers(2195, "ALL", "BME"))
    # pretty_print(tufts_courses.performSearch(2192, subject="ENG", crs_number="0001"))
    # print(tufts_courses.getCareer().text);
    
if __name__=="__main__":
    main()
