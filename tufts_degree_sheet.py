#!/usr/bin/python3
from enum import Enum, unique


@unique
class Category(Enum):
    INTRO = 0
    HASS = 1
    BREADTH = 2
    FOUNDATION = 3
    CONCENTRATION = 4
    FREE_ELECTIVe = 5


CS_2019 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
CS_2020 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
CS_2021 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
CS_2022 = {
    "intro": {
        "courses": [
            ["EN-0001"],
            ["ES-0002"],
            ["MATH-0032"],
            ["MATH-0034", "MATH-0039"],
            ["MATH-0042", "MATH-0044"],
            ["MATH-0061", "COMP-0061"],
            ["PHY-0011"],
            ["CHEM-0001"]
        ],
        "attributes": [
            ["SoE-Natural Sciences"],
            ["SoE-Natural Sciences"]
        ]
    },
    "hass":  {
        "courses": [
            ["ENG-0001", "ENG-0003"],
        ],
        "attributes": [
            ["SoE-HASS-Social Sciences"],
            ["SoE-HASS-Humanities"],
            ["SoE-HASS"],
            ["SoE-HASS"]
        ]
    },
    "breadth": {
        "courses": [
            ["PHIL-0024", "EM-0054"]
        ],
        "attributes": []
    },
    "foundation": {
        "courses": [
            ["ES-0003"],
            ["ES-0004"],
            ["COMP-0011"],
            ["COMP-0015"],
            ["MATH-0162", "ES-0056", "EE-0024", "EE-0104",
             "BME-0104", "BIO-0132", "PHY-0153"]
            # ["MATH-0070", "MATH-0072"],
        ],
        "attributes": []
    },
    "concentration": {
        "courses": [
            #Required
            ["COMP-0040"],
            ["COMP-0105", "COMP-0080"],
            ["COMP-0160"],
            ["COMP-0170"],
            #Electives
            ["COMP-0111"], # e compsci 100-189
            ["COMP-0122"], # e compsci 100-189
            ["COMP-0055", "COMP-0116", "COMP-0120", "COMP-0155"],
            ["COMP-0093","COMP-0094","COMP-0191","COMP-0193","COMP-0194","COMP-0197"],
            ["MATH-0051", "MATH-0063", "MATH-0070", "MATH-0072", "MATH-0087", "MATH-0135", "MATH-0136", "MATH-0145", "MATH-0146", "MATH-0151", "MATH-0152", "MATH-0158", "MATH-0161", "MATH-0162"],
            #Senior Design
            ["COMP-97"],
            ["COMP-98"]
        ],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
CS_2023 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}


CE_2019 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
CE_2020 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
CE_2021 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}


CE_2022 = {
    "intro": {
        "courses": [
            ["MATH-0032"],
            ["MATH-0034", "MATH-0036"],
            ["MATH-0042"],
            ["MATH-0051"],
            ["PHY-0011"],
            ["PHY-0012"],
            ["CHEM-0001"],
            ["EN-0001"],
            ["ES-0002"]
        ],
        "attributes": [
            ["SoE-Natural Sciences"]
        ]
    },
    "hass":  {
        "courses": [
            ["ENG-0001", "ENG-0003"],
        ],
        "attributes": [
            ["SoE-HASS-Social Sciences"],
            ["SoE-HASS-Humanities"],
            ["SoE-HASS"],
            ["SoE-HASS"]
        ]
    },
    "foundation": {
        "courses": [
            ["ES-0004"],
            ["ES-0003"],
            ["EE-0023"],
            ["EE-0024"],
            ["MATH-0061"],
            ["MATH-0070", "MATH-0072"],
            ["COMP-0011"],
            ["COMP-0015"]
        ],
        "attributes": []
    },
    "concentration": {
        "courses": [
            ["EE-0014"],
            ["EE-0021"],
            ["EE-0026"],
            ["EE-0031"],
            ["EE-0103"],
            ["EE-0126"],
            ["EE-0128"],
            ["EE-0097"],
            ["EE-0098"]
        ],
        "attributes": [
            ["SoE-Engineering"],
            ["SoE-Engineering"],
            ["SoE-Engineering"],
            ["SoE-Engineering"]
        ]
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
CE_2023 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}


EE_2019 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
EE_2020 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
EE_2021 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
EE_2022 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
EE_2023 = {
    "intro": {
        "courses": [],
        "attributes": []
    },
    "hass":  {
        "courses": [],
        "attributes": []
    },
    "breadth": {
        "courses": [],
        "attributes": []
    },
    "foundation": {
        "courses": [],
        "attributes": []
    },
    "concentration": {
        "courses": [],
        "attributes": []
    },
    "free_elective": {
        "courses": [],
        "attributes": []
    }
}
