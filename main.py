from PIL import Image 
from IPython.display import display 
import random
import json

ART_IMAGES = ["Aynor Jungle", "Magical Tower of Hyth", "The Arch Place", "Ral’genor", "The Kulun Temple", "Sarenys"]
ART_IMAGE_FILES = {
    "Aynor Jungle": "aynor_jungle", 
    "Magical Tower of Hyth": "magical_tower_hyth", 
    "The Arch Place": "arch_place", 
    "Ral’genor": "ral_genor", 
    "The Kulun Temple": "kulun_temple", 
    "Sarenys": "sarenys"
}

TRAITS = [
    [
        [
            {
                "trait_type": "Merchant Prices",
                "value": "-3%"
            }
        ],
        [
            {
                "trait_type": "Defense",
                "value": "+1"
            }
        ],
        [
            {
                "trait_type": "Dexterity",
                "value": "+1"
            }
        ]
    ],
    [
        [
            {
                "trait_type": "Magical Defense",
                "value": "+1"
            }
        ],
        [
            {
                "trait_type": "Strength",
                "value": "+1"
            }
        ],
        [
            {
                "trait_type": "Merchant Prices",
                "value": "-5%"
            }
        ]
    ],
    [
        [
            {
                "trait_type": "Melee Weapon Damage",
                "value": "+5%"
            },
            {
                "trait_type": "Strength",
                "value": "+1"
            }
        ],
        [
            {
                "trait_type": "Magic Weapon Damage",
                "value": "+5%"
            },
            {
                "trait_type": "Intelligence",
                "value": "+1"
            }
        ],
        [
            {
                "trait_type": "Constitution",
                "value": "+2"
            }
        ]
    ],
    [
        [
            {
                "trait_type": "Melee Damage Taken",
                "value": "-5%"
            }
        ],
        [
            {
                "trait_type": "Magic Damage Taken",
                "value": "-5%"
            }
        ],
        [
            {
                "trait_type": "Damage Taken",
                "value": "-3%"
            }
        ]
    ],
    [
        [
            {
                "trait_type": "All Skills",
                "value": "+1"
            },
            {
                "trait_type": "Attack Speed",
                "value": "+5%"
            },
            {
                "trait_type": "Constitution",
                "value": "+1"
            }
        ],
        [
            {
                "trait_type": "Magic Defense",
                "value": "+3"
            },
            {
                "trait_type": "All Skills",
                "value": "+1"
            }
        ],
        [
            {
                "trait_type": "Damage Taken",
                "value": "-5%"
            },
            {
                "trait_type": "Constitution",
                "value": "+2"
            }
        ]
    ]
]

TRAITS_COUNT = 5
ARTS_COUNT = [500, 250, 125, 90, 35]
TRAITS_WEIGHT = [33.33, 33.33, 33.34]

all_images = []
index = 0

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

for art_image in ART_IMAGES:
    for i in range(TRAITS_COUNT):
        for j in range(ARTS_COUNT[i]):
            metadata = {
                "name": f'Era Spheres Lands #{index + 1}',
                "symbol": "ERA LANDS",
                "description": "Era Spheres: The Land Collection of Era Spheres is comprised of 6000 NFT all with different rarities and in-game bonuses.",
                "seller_fee_basis_points": 250,
                "image": f'{index}.png',
                "external_url": "https://eraspheres.com/",
                "attributes": [],
                "collection": {
                    "name": "Era Spheres Lands",
                    "family": "EraSpheresLands"
                },
                "properties": {
                    "files": [
                        {
                            "uri": f'{index}.png',
                            "type": "image/png"
                        }
                    ],
                    "category": "image",
                    "creators": [
                        {
                            "share": 100,
                            "address": "7ot3DaniokiprHGSW29xs9oR7ibu2CcvjXoQs9iDbx2M"
                        }
                    ]
                }
            }
            
            traits = TRAITS[i]
            trait = random.choices(traits, TRAITS_WEIGHT)[0]
            for item in trait:
                metadata["attributes"].append(item)
            metadata["attributes"].append(getAttribute("Type", art_image))

            with open("./metadata/" + str(index) + ".json", "w") as outfile:
                json.dump(metadata, outfile, indent=4)

            # image = Image.open(f'./trait-layers/arts/{ART_IMAGE_FILES[art_image]}.png').convert('RGBA')
            # file_name = str(index) + ".png"
            # image.save("./images/" + file_name)

            index += 1
