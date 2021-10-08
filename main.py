from PIL import Image 
from IPython.display import display 
import random
import json

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%
leaderpunk = ["LeaderPunk"]
leaderpunk_weights = [100]

background_color = ["Blue", "Baby-Blue", "Bright-Pink", "Bright-Purple", "Bright-Red", "Bright-Violet", "Dark-Green", "Dark-Lilac", "Dark-Pink", "Dirt", "Gray", "Green", "Light-Blue", "Light-Dirt", "Lilac", "Lime-Green", "Mint", "Ochre", "Orange", "Pastel-Blue", "Pastel-Lilac", "Pastel-Orange", "Pastel-Purple", "Pastel-Violet", "Pink", "Purple", "Red", "Sunshine-Yellow", "Toxic-Green", "White", "Wine-Red", "Yellow"] 
background_color_weights = [5, 1, 3, 1, 2, 4, 3, 3, 8, 10, 2, 3, 5, 5, 4, 4, 3 ,4 , 6, 2, 1, 1, 2, 5, 2, 1, 1, 1, 1, 2, 1, 4 ]

hat = ["Green", "Purple", "Red", "Yellow"] 
hat_weights = [50, 20, 10, 20]

necklace = ["Amber", "Amethyst", "Lapislazuli", "Ruby", "Smaragd"] 
necklace_weights = [30, 40, 5, 20, 5]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name

background_color_files = {
    "Blue": "blue",
    "Baby-Blue": "baby-blue",
    "Bright-Pink": "bright-pink",
    "Bright-Purple": "bright-purple",
    "Bright-Red": "bright-red",
    "Bright-Violet": "bright-violet",
    "Dark-Green": "dark-green",
    "Dark-Lilac": "dark-lilac",
    "Dark-Pink": "dark-pink",
    "Dirt": "dirt", 
    "Gray": "gray",
    "Green": "green",
    "Light-Blue": "light-blue",
    "Light-Dirt": "light-dirt",
    "Light-Yellow": "light-yellow",
    "Lilac": "lilac",
    "Lime-Green": "lime-green",
    "Mint": "mint",
    "Ochre": "ochre",
    "Orange": "orange",
    "Pastel-Blue": "pastel-blue",
    "Pastel-Lilac": "pastel-lilac",
    "Pastel-Orange": "pastel-orange",
    "Pastel-Purple": "pastel-purple",
    "Pastel-Violet": "pastel-violet",
    "Pink": "pink",
    "Purple": "purple",
    "Red": "red",
    "Sunshine-Yellow": "sunshine-yellow",
    "Toxic-Green": "toxic-green",
    "White": "white",
    "Wine-Red": "wine-red",
    "Yellow": "yellow",
}

leaderpunk_files = {
    "LeaderPunk": "leaderpunk"
}

hat_files = {
    "Green": "green-hat",
    "Purple": "purple-hat",
    "Red": "red-hat",
    "Yellow": "yellow-hat"   
}

necklace_files = {
    "Amber": "amber-necklace",
    "Amethyst": "amethyst-necklace",
    "Lapislazuli": "lapislazuli-necklace",
    "Ruby": "ruby-necklace",
    "Smaragd": "smaragd-necklace"  
}

## Generate Traits
TOTAL_IMAGES = 30 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background-Color"] = random.choices(background_color, background_color_weights)[0]
    new_image ["LeaderPunk"] = random.choices(leaderpunk, leaderpunk_weights)[0]
    new_image ["Hat"] = random.choices(hat, hat_weights)[0]
    new_image ["Necklace"] = random.choices(necklace, necklace_weights)[0]
    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)
	
# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)

# Get Trait Counts
background_color_count = {}
for item in background_color:
    background_color_count[item] = 0
    
leaderpunk_count = {}
for item in leaderpunk:
    leaderpunk_count[item] = 0

hat_count = {}
for item in hat:
    hat_count[item] = 0

necklace_count = {}
for item in necklace:
    necklace_count[item] = 0

for image in all_images:
    background_color_count[image["Background-Color"]] += 1
    leaderpunk_count[image["LeaderPunk"]] += 1
    hat_count[image["Hat"]] += 1
    necklace_count[image["Necklace"]] += 1
    
print(background_color_count)
print(leaderpunk_count)
print(hat_count)
print(necklace_count)

#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

#### Generate Images    
for item in all_images:

    im1 = Image.open(f'./trait-layers/backgrounds/{background_color_files[item["Background-Color"]]}.png').convert('RGBA')
    im2 = Image.open(f'./trait-layers/leaderpunk/{leaderpunk_files[item["LeaderPunk"]]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/hats/{hat_files[item["Hat"]]}.png').convert('RGBA')
    im4 = Image.open(f'./trait-layers/necklaces/{necklace_files[item["Necklace"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(im3, im4)
    com3 = Image.alpha_composite(com1, com2)


    #Convert to RGB
    rgb_im = com3.convert('RGBA')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
	
#### Generate Metadata for each Image    
f = open('./metadata/all-traits.json',) 
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ADD_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background-Color", i["Background-Color"]))
    token["attributes"].append(getAttribute("LeaderPunk", i["LeaderPunk"]))
    token["attributes"].append(getAttribute("Hat", i["Hat"]))
    token["attributes"].append(getAttribute("Necklace", i["Necklace"]))

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()