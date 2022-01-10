from PIL import Image 
from IPython.display import display 
import random
import json

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%
backgrounds = ["Bananas", "Blue", "Brown", "City Daytime", "City Nighttime", "Clouds", "Galaxy", "Green", "Grey", "Jungle", "Olive", "Orange", "Pink", "Purple", "Rainbow", "Red", "Sky", "Yellow"]
background_weights = [2.65, 10.54, 11.53, 2.79, 1.65, 2.05, 0.2, 5.18, 10, 2.64, 8.11, 5.85, 4.75, 7.59, 0.69, 8.12, 6.79, 8.87]
background_files = {
    "Bananas": "Bananas.png",
    "Blue": "Blue.png",
    "Brown": "Brown.png",
    "City Daytime": "City_Day.png",
    "City Nighttime": "City_Night.png",
    "Clouds": "Clouds.png",
    "Galaxy": "Galaxy.png",
    "Green": "Green.png",
    "Grey": "Grey.png",
    "Jungle": "Jungle.png",
    "Olive": "Olive.png",
    "Orange": "Orange.png",
    "Pink": "Pink.png",
    "Purple": "Purple.png",
    "Rainbow": "Rainbow.png",
    "Red": "Red.png",
    "Sky": "Sky.png",
    "Yellow": "Yellow.png"
}

clothes = ["None", "Red Hoodie", "Aladdin monkey vest", "Bow tie", "Dog Tags", "Brown Dog Collar", "Mechanic Overalls", "Black Hoodie", "Pine Green Crewneck", "Gorilla Warfare Vest", "Orange Hoodie", "Banana tie", "Red Dog Collar", "Ruff collar", "GG Tie", "Prison jumpsuit", "Gold Chain", "Neck Spiked Collar", "Solana Hoodie", "Galaxy Mechanic Overalls", "Saiyan armour Original", "Saiyan Armour black & red", "Skeleton Outfit", "GG Chain"]
cloth_weights = [27.8, 11.4, 5.5, 4.9, 6.8, 6.3, 4.8, 3.2, 3.4, 2.6, 3.1, 3.0, 3.6, 2.9, 2.5, 1.6, 1.5, 2.4, 0.15, 0.8, 0.33, 0.25, 0.5, 0.67]
cloth_files = {
    "None": "None.png",
    "Red Hoodie": "Red_Hoodie.png",
    "Aladdin monkey vest": "Vest.png",
    "Bow tie": "Bow_Tie.png",
    "Dog Tags": "Dog_Tag.png",
    "Brown Dog Collar": "Brown_Dog_Collar.png",
    "Mechanic Overalls": "Mechanic_Overalls.png",
    "Black Hoodie": "Black_Hoodie.png",
    "Pine Green Crewneck": "Green_Crewneck.png",
    "Gorilla Warfare Vest": "Gorilla_Warfare_Vest.png",
    "Orange Hoodie": "Orange_Hoodie.png",
    "Banana tie": "Banana_Tie.png",
    "Red Dog Collar": "Red_Dog_Collar.png",
    "Ruff collar": "Ruff_Collar.png",
    "GG Tie": "GG_Tie.png",
    "Prison jumpsuit": "Prison_Jumpsuit.png",
    "Gold Chain": "Gold_Chain.png",
    "Neck Spiked Collar": "Spiked_Collar.png",
    "Solana Hoodie": "Solana_Hoodie.png",
    "Galaxy Mechanic Overalls": "Galaxy_Mechanic_Overalls.png",
    "Saiyan armour Original": "Galaxy_Defender_Armor.png",
    "Saiyan Armour black & red": "Galaxy_Fighter_Armor.png",
    "Skeleton Outfit": "Skeleton_Outfit.png",
    "GG Chain": "GG_Chain.png",
}

earrings = ["None", "Silver", "Gold", "Diamond"]
earring_weights = [80.66, 11.65, 6.37, 1.32]
earring_files = {
    "None": "None.png",
    "Silver": "Silver.png",
    "Gold": "Gold.png",
    "Diamond": "Diamond.png"
}

eyewears = ["None", "Small Round Glasses", "Black Sunglasses", "Crossed Out", "Purple Square glasses", "Tired", "X-ray spex", "3D glasses", "Crying", "Dollar Sign", "Whiteout", "Eyepatch", "Face Screen", "Third Eye", "Cyclops", "White Shutter Shades", "Hypno Glasses", "Night Vision Goggles", "Orange Shutter Shades", "Hologram Glasses", "Scar", "Mirror Wheel", "Pit Visors", "Power Scanner", "Cyclops Visor", "Kawaii Eyes", "Primal Eyes", "Cyborg", "Red Laser", "Blue Laser", "Cyborg Spider"]
eyewear_weights = [31.59, 5.18, 4.76, 4.26, 4.2, 4.05, 3.74, 3.63, 3.32, 3.09, 2.97, 2.86, 2.76, 2.54, 2.40, 2.29, 2.26, 2.23, 2.11, 2.04, 2.01, 1.87, 1.79, 0.45, 0.44, 0.34, 0.23, 0.2, 0.17, 0.15, 0.07]
eyewear_files = {
    "None": "None.png",
    "Small Round Glasses": "Small_Round_Glasses.png",
    "Black Sunglasses": "Black_Sunglasses.png",
    "Crossed Out": "Crossed_Out",
    "Purple Square glasses": "Purple_Square_Glasses.png",
    "Tired": "Tired",
    "X-ray spex": "Xray_Spex.png",
    "3D glasses": "3D_Glasses.png",
    "Crying": "Crying",
    "Dollar Sign": "Dollar_Sign",
    "Whiteout": "Whiteout.png",
    "Eyepatch": "Eyepatch.png",
    "Face Screen": "Face_Screen.png",
    "Third Eye": "Third_Eye",
    "Cyclops": "Cyclops",
    "White Shutter Shades": "White_Shutter_Shades.png",
    "Hypno Glasses": "Hypno_Glasses.png",
    "Night Vision Goggles": "Night_Vision_Goggles.png",
    "Orange Shutter Shades": "Orange_Shutter_Shades.png",
    "Hologram Glasses": "Hologram_Glasses.png",
    "Scar": "Scar.png",
    "Mirror Wheel": "Mirror_Wheel.png",
    "Pit Visors": "Pit_Visors.png",
    "Power Scanner": "Power_Scanner.png",
    "Cyclops Visor": "Cyclops_Visor.png",
    "Kawaii Eyes": "Kawaii",
    "Primal Eyes": "Primal",
    "Cyborg": "Cyborg.png",
    "Red Laser": "Red_Laser.png",
    "Blue Laser": "Blue_Laser.png",
    "Cyborg Spider": "Cyborg_Spider.png"
}

furs = ["Grey", "Brown", "Green", "Tan", "Orange", "Black", "Blue", "Red", "Purple", "Albino", "Neon", "Metal"]
fur_weights = [15.59, 12.47, 11.83, 11.02, 10.13, 8.46, 8, 7.7, 7.36, 3.9, 3.29, 0.25]
fur_files = {
    "Grey": "Fur_Grey.png",
    "Brown": "Fur_Brown.png",
    "Green": "Fur_Green.png",
    "Tan": "Fur_Tan.png",
    "Orange": "Fur_Orange.png",
    "Black": "Fur_Black.png",
    "Red": "Fur_Red.png",
    "Blue": "Fur_Blue.png",
    "Purple": "Fur_Purple.png",
    "Albino": "Fur_Albino.png",
    "Neon": "Fur_Neon.png",
    "Metal": "Fur_Metal.png",
}

hats = ["None", "Black Fisherman Beanie", "Bucket Hat White", "Bucket Hat Purple", "Fez", "Bowler hat", "Red Cap", "Backwards cap blue", "Helicopter Kids Hat", "Hard Hat", "Safari Hat", "70s Visor", "Mini Sailor Hat", "Straw Hat", "Banana Peel", "Aviator Hat", "Bright Green Bucket Hat", "Light Blue Fisherman Beanie", "Rice Farmer Hat", "Police Cap", "Blue Escape Hat", "Black Durag", "Wizard Hat", "Mojo GoGo Hat", "Red Escape Hat", "Cogwheel Crown", "Chief Helmet", "Banana Tape", "Mini Bowler Hat", "Rainbow Durag", "Halo", "Mini Monkey", "Exposed Brain"]
hat_weights = [14.02, 6.66, 5.33, 5.21, 4.99, 4.79, 4.66, 4.48, 4.12, 3.96, 3.75, 3.45, 3.39, 3.19, 3.11, 2.99, 2.78, 2.44, 2.22, 2.11, 2, 1.89, 1.8, 1.5, 1.2, 1.14, 0.8, 0.65, 0.48, 0.33, 0.23, 0.23, 0.1]
hat_files = {
    "None": "None.png",
    "Black Fisherman Beanie": "Black_Fisherman_Beanie.png",
    "Bucket Hat White": "White_Bucket_Hat.png",
    "Bucket Hat Purple": "Purple_Bucket_Hat.png",
    "Fez": "Fez.png",
    "Bowler hat": "Bowler_Hat.png",
    "Red Cap": "Red_Cap.png",
    "Backwards cap blue": "Blue_Backwards_Cap.png",
    "Helicopter Kids Hat": "Helicopter_Hat.png",
    "Hard Hat": "Hard_Hat.png",
    "Safari Hat": "Safari_Hat.png",
    "70s Visor": "70s_Visor.png",
    "Mini Sailor Hat": "Mini_Sailor_Hat.png",
    "Straw Hat": "Straw_Hat.png",
    "Banana Peel": "Banana_Peel.png",
    "Aviator Hat": "Aviator_Hat.png",
    "Bright Green Bucket Hat": "Green_Bucket_Hat.png",
    "Light Blue Fisherman Beanie": "Blue_Fisherman_Beanie.png",
    "Rice Farmer Hat": "Rice_Farmer_Hat.png",
    "Police Cap": "Police_Cap.png",
    "Blue Escape Hat": "Blue_Escape_Hat.png",
    "Black Durag": "Black_Durag.png",
    "Wizard Hat": "Wizard_Hat.png",
    "Mojo GoGo Hat": "Mojo_GoGo.png",
    "Red Escape Hat": "Red_Escape_Hat.png", 
    "Cogwheel Crown": "Cogwheel_Crown.png",
    "Chief Helmet": "Chief_Helmet.png",
    "Banana Tape": "Taped_Banana.png",
    "Mini Bowler Hat": "Mini-Bowler_Hat.png",
    "Rainbow Durag": "Rainbow_Durag.png",
    "Halo": "Halo.png",
    "Mini Monkey": "Mini_Monkey.png",
    "Exposed Brain": "Exposed_Brain.png"
}

mouthes = ["None", "Bamboo Straw", "Drool", "Bubblegum", "Cigarettes", "Face Mask", "Vape", "Banana", "Biting on knife", "Oh Mouth", "Grenade", "Wooden Pipe", "Big Fat Tongue", "Toothy Grin", "Silver Grillz", "Pacifier", "Gold Grillz", "Below Freezing"]
mouth_weights = [35.95, 7.21, 6.89, 6.55, 6.22, 5.25, 5.1, 4.57, 4.33, 4, 3.67, 2.99, 2.55, 1.88, 1.58, 0.88, 0.27, 0.11]
mouth_files = {
    "None": "None.png",
    "Bamboo Straw": "Bamboo.png",
    "Drool": "Drool.png",
    "Bubblegum": "Bubblegum.png",
    "Cigarettes": "Cigarette.png",
    "Face Mask": "Face_Mask.png",
    "Vape": "Vape.png",
    "Banana": "Banana",
    "Biting on knife": "Knife",
    "Oh Mouth": "OH",
    "Grenade": "Grenade",
    "Wooden Pipe": "Wooden_Pipe",
    "Big Fat Tongue": "Tongue.png",
    "Toothy Grin": "Toothy_Grin",
    "Silver Grillz": "Silver_Grillz",
    "Pacifier": "Pacifier",
    "Gold Grillz": "Gold_Grillz",
    "Below Freezing": "Below_Zero.png"
}

eyes_crossed_out_files = {
    "Albino": "Crossed_Out_Albino.png",
    "Black": "Crossed_Out_Black.png",
    "Blue": "Crossed_Out_Blue.png",
    "Brown": "Crossed_Out_Brown.png",
    "Green": "Crossed_Out_Green.png",
    "Grey": "Crossed_Out_Grey.png",
    "Metal": "Crossed_Out_Metal.png",
    "Neon": "Crossed_Out_Neon.png",
    "Orange": "Crossed_Out_Orange.png",
    "Purple": "Crossed_Out_Purple.png",
    "Red": "Crossed_Out_Red.png",
    "Tan": "Crossed_Out_Tan.png"
}

eyes_tired_files = {
    "Albino": "Tired_Albino.png",
    "Blue": "Tired_Blue_Black_Green_Red_Orange.png",
    "Black": "Tired_Blue_Black_Green_Red_Orange.png",
    "Green": "Tired_Blue_Black_Green_Red_Orange.png",
    "Red": "Tired_Blue_Black_Green_Red_Orange.png",
    "Orange": "Tired_Blue_Black_Green_Red_Orange.png",
    "Metal": "Tired_Metal.png",
    "Neon": "Tired_Neon.png",
    "Tan": "Tired_Tan_Brown_Purple_Grey.png",
    "Brown": "Tired_Tan_Brown_Purple_Grey.png",
    "Purple": "Tired_Tan_Brown_Purple_Grey.png",
    "Grey": "Tired_Tan_Brown_Purple_Grey.png"
}

eyes_crying_files = {
    "Albino": "Crying_Albino.png",
    "Black": "Crying_Black.png",
    "Blue": "Crying_Blue.png",
    "Brown": "Crying_Brown.png",
    "Green": "Crying_Green.png",
    "Grey": "Crying_Grey.png",
    "Metal": "Crying_Metal.png",
    "Neon": "Crying_Neon.png",
    "Orange": "Crying_Orange.png",
    "Purple": "Crying_Purple.png",
    "Red": "Crying_Red.png",
    "Tan": "Crying_Tan.png"
}

eyes_dollar_sign_files = {
    "Albino": "Dollar_Sign_Albino.png",
    "Blue": "Dollar_Sign_Blue_Black_Green_Red_Orange.png",
    "Black": "Dollar_Sign_Blue_Black_Green_Red_Orange.png",
    "Green": "Dollar_Sign_Blue_Black_Green_Red_Orange.png",
    "Red": "Dollar_Sign_Blue_Black_Green_Red_Orange.png",
    "Orange": "Dollar_Sign_Blue_Black_Green_Red_Orange.png",
    "Metal": "Dollar_Sign_Metal.png",
    "Neon": "Dollar_Sign_Neon.png",
    "Tan": "Dollar_Sign_Tan_Brown_Purple_Grey.png",
    "Brown": "Dollar_Sign_Tan_Brown_Purple_Grey.png",
    "Purple": "Dollar_Sign_Tan_Brown_Purple_Grey.png",
    "Grey": "Dollar_Sign_Tan_Brown_Purple_Grey.png"
}

eyes_third_eye_files = {
    "Albino": "Third_Eye_Albino.png",
    "Black": "Third_Eye_Black.png",
    "Blue": "Third_Eye_Blue.png",
    "Brown": "Third_Eye_Brown.png",
    "Green": "Third_Eye_Green.png",
    "Grey": "Third_Eye_Grey.png",
    "Metal": "Third_Eye_Metal.png",
    "Neon": "Third_Eye_Neon.png",
    "Orange": "Third_Eye_Orange.png",
    "Purple": "Third_Eye_Purple.png",
    "Red": "Third_Eye_Red.png",
    "Tan": "Third_Eye_Tan.png"
}

eyes_cyclops_files = {
    "Albino": "Cyclops_Albino.png",
    "Blue": "Cyclops_Black_Green_Red_Orange.png",
    "Black": "Cyclops_Black_Green_Red_Orange.png",
    "Green": "Cyclops_Black_Green_Red_Orange.png",
    "Red": "Cyclops_Black_Green_Red_Orange.png",
    "Orange": "Cyclops_Black_Green_Red_Orange.png",
    "Metal": "Cyclops_Metal.png",
    "Neon": "Cyclops_Neon.png",
    "Tan": "Cyclops_Tan_Brown_Purple_Grey.png",
    "Brown": "Cyclops_Tan_Brown_Purple_Grey.png",
    "Purple": "Cyclops_Tan_Brown_Purple_Grey.png",
    "Grey": "Cyclops_Tan_Brown_Purple_Grey.png"
}

eyes_kawaii_files = {
    "Albino": "Kawaii_Albino.png",
    "Blue": "Kawaii_Blue_Black_Green_Red_Orange.png",
    "Black": "Kawaii_Blue_Black_Green_Red_Orange.png",
    "Green": "Kawaii_Blue_Black_Green_Red_Orange.png",
    "Red": "Kawaii_Blue_Black_Green_Red_Orange.png",
    "Orange": "Kawaii_Blue_Black_Green_Red_Orange.png",
    "Metal": "Kawaii_Metal.png",
    "Neon": "Kawaii_Neon.png",
    "Tan": "Kawaii_Tan_Brown_Purple_Grey.png",
    "Brown": "Kawaii_Tan_Brown_Purple_Grey.png",
    "Purple": "Kawaii_Tan_Brown_Purple_Grey.png",
    "Grey": "Kawaii_Tan_Brown_Purple_Grey.png"
}

eyes_primal_files = {
    "Albino": "Primal_Albino.png",
    "Blue": "Primal_Blue_Black_Green_Red_Orange.png",
    "Black": "Primal_Blue_Black_Green_Red_Orange.png",
    "Green": "Primal_Blue_Black_Green_Red_Orange.png",
    "Red": "Primal_Blue_Black_Green_Red_Orange.png",
    "Orange": "Primal_Blue_Black_Green_Red_Orange.png",
    "Metal": "Primal_Metal.png",
    "Neon": "Primal_Neon.png",
    "Tan": "Primal_Tan_Brown_Purple_Grey.png",
    "Brown": "Primal_Tan_Brown_Purple_Grey.png",
    "Purple": "Primal_Tan_Brown_Purple_Grey.png",
    "Grey": "Primal_Tan_Brown_Purple_Grey.png"
}

mouth_banana_files = {
    "Albino": "Banana_Albino.png",
    "Blue": "Banana_Blue_Black_Green_Red_Orange.png",
    "Black": "Banana_Blue_Black_Green_Red_Orange.png",
    "Green": "Banana_Blue_Black_Green_Red_Orange.png",
    "Red": "Banana_Blue_Black_Green_Red_Orange.png",
    "Orange": "Banana_Blue_Black_Green_Red_Orange.png",
    "Metal": "Banana_Metal.png",
    "Neon": "Banana_Neon.png",
    "Tan": "Banana_Tan_Brown_Purple_Grey.png",
    "Brown": "Banana_Tan_Brown_Purple_Grey.png",
    "Purple": "Banana_Tan_Brown_Purple_Grey.png",
    "Grey": "Banana_Tan_Brown_Purple_Grey.png"
}

mouth_Knife_files = {
    "Albino": "Knife_Albino.png",
    "Blue": "Knife_Blue_Black_Green_Red_Orange.png",
    "Black": "Knife_Blue_Black_Green_Red_Orange.png",
    "Green": "Knife_Blue_Black_Green_Red_Orange.png",
    "Red": "Knife_Blue_Black_Green_Red_Orange.png",
    "Orange": "Knife_Blue_Black_Green_Red_Orange.png",
    "Metal": "Knife_Metal.png",
    "Neon": "Knife_Neon.png",
    "Tan": "Knife_Tan_Brown_Purple_Grey.png",
    "Brown": "Knife_Tan_Brown_Purple_Grey.png",
    "Purple": "Knife_Tan_Brown_Purple_Grey.png",
    "Grey": "Knife_Tan_Brown_Purple_Grey.png"
}

mouth_OH_files = {
    "Albino": "OH_Albino.png",
    "Blue": "OH_Blue_Black_Green_Red_Orange.png",
    "Black": "OH_Blue_Black_Green_Red_Orange.png",
    "Green": "OH_Blue_Black_Green_Red_Orange.png",
    "Red": "OH_Blue_Black_Green_Red_Orange.png",
    "Orange": "OH_Blue_Black_Green_Red_Orange.png",
    "Metal": "OH_Metal.png",
    "Neon": "OH_Neon.png",
    "Tan": "OH_Tan_Brown_Purple_Grey.png",
    "Brown": "OH_Tan_Brown_Purple_Grey.png",
    "Purple": "OH_Tan_Brown_Purple_Grey.png",
    "Grey": "OH_Tan_Brown_Purple_Grey.png"
}

mouth_grenade_files = {
    "Albino": "Grenade_Albino.png",
    "Blue": "Grenade_Blue_Black_Green_Red_Orange.png",
    "Black": "Grenade_Blue_Black_Green_Red_Orange.png",
    "Green": "Grenade_Blue_Black_Green_Red_Orange.png",
    "Red": "Grenade_Blue_Black_Green_Red_Orange.png",
    "Orange": "Grenade_Blue_Black_Green_Red_Orange.png",
    "Metal": "Grenade_Metal.png",
    "Neon": "Grenade_Neon.png",
    "Tan": "Grenade tan brown purple grey.png",
    "Brown": "Grenade tan brown purple grey.png",
    "Purple": "Grenade tan brown purple grey.png",
    "Grey": "Grenade tan brown purple grey.png"
}

mouth_wooden_pipe_files = {
    "Albino": "Wooden Pipe albino.png",
    "Blue": "Wooden_Pipe_Blue_Black_Green_Red_Orange.png",
    "Black": "Wooden_Pipe_Blue_Black_Green_Red_Orange.png",
    "Green": "Wooden_Pipe_Blue_Black_Green_Red_Orange.png",
    "Red": "Wooden_Pipe_Blue_Black_Green_Red_Orange.png",
    "Orange": "Wooden_Pipe_Blue_Black_Green_Red_Orange.png",
    "Metal": "Wooden Pipe metal.png",
    "Neon": "Wooden Pipe neon.png",
    "Tan": "Wooden_Pipe_Tan_Brown_Purple_Grey.png",
    "Brown": "Wooden_Pipe_Tan_Brown_Purple_Grey.png",
    "Purple": "Wooden_Pipe_Tan_Brown_Purple_Grey.png",
    "Grey": "Wooden_Pipe_Tan_Brown_Purple_Grey.png"
}

mouth_toothy_grin_files = {
    "Albino": "Toothy_Grin_Albino.png",
    "Blue": "Toothy_Grin_Blue_Black_Green_Red_Orange.png",
    "Black": "Toothy_Grin_Blue_Black_Green_Red_Orange.png",
    "Green": "Toothy_Grin_Blue_Black_Green_Red_Orange.png",
    "Red": "Toothy_Grin_Blue_Black_Green_Red_Orange.png",
    "Orange": "Toothy_Grin_Blue_Black_Green_Red_Orange.png",
    "Metal": "Toothy_Grin_Metal.png",
    "Neon": "Toothy_Grin_Neon.png",
    "Tan": "Toothy_Grin_Tan_Brown_Purple_Grey.png",
    "Brown": "Toothy_Grin_Tan_Brown_Purple_Grey.png",
    "Purple": "Toothy_Grin_Tan_Brown_Purple_Grey.png",
    "Grey": "Toothy_Grin_Tan_Brown_Purple_Grey.png"
}

mouth_silver_grillz_files = {
    "Albino": "Silver_Grillz_Albino.png",
    "Blue": "Silver_Grillz_Blue_Black_Green_Red_Orange.png",
    "Black": "Silver_Grillz_Blue_Black_Green_Red_Orange.png",
    "Green": "Silver_Grillz_Blue_Black_Green_Red_Orange.png",
    "Red": "Silver_Grillz_Blue_Black_Green_Red_Orange.png",
    "Orange": "Silver_Grillz_Blue_Black_Green_Red_Orange.png",
    "Metal": "Silver_Grillz_Metal.png",
    "Neon": "Silver_Grillz_Neon.png",
    "Tan": "Silver_Grillz_Tan_Brown_Purple_Grey.png",
    "Brown": "Silver_Grillz_Tan_Brown_Purple_Grey.png",
    "Purple": "Silver_Grillz_Tan_Brown_Purple_Grey.png",
    "Grey": "Silver_Grillz_Tan_Brown_Purple_Grey.png"
}

mouth_pacifier_files = {
    "Albino": "Pacifier_Albino.png",
    "Blue": "Pacifier_Blue_Black_Green_Red_Orange.png",
    "Black": "Pacifier_Blue_Black_Green_Red_Orange.png",
    "Green": "Pacifier_Blue_Black_Green_Red_Orange.png",
    "Red": "Pacifier_Blue_Black_Green_Red_Orange.png",
    "Orange": "Pacifier_Blue_Black_Green_Red_Orange.png",
    "Metal": "Pacifier_Metal.png",
    "Neon": "Pacifier_Neon.png",
    "Tan": "Pacifier_Tan_Brown_Purple_Grey.png",
    "Brown": "Pacifier_Tan_Brown_Purple_Grey.png",
    "Purple": "Pacifier_Tan_Brown_Purple_Grey.png",
    "Grey": "Pacifier_Tan_Brown_Purple_Grey.png"
}

mouth_gold_grillz_files = {
    "Albino": "Gold_Grillz_Albino.png",
    "Blue": "Gold_Grillz_Black_Blue_Green_Red_Orange.png",
    "Black": "Gold_Grillz_Black_Blue_Green_Red_Orange.png",
    "Green": "Gold_Grillz_Black_Blue_Green_Red_Orange.png",
    "Red": "Gold_Grillz_Black_Blue_Green_Red_Orange.png",
    "Orange": "Gold_Grillz_Black_Blue_Green_Red_Orange.png",
    "Metal": "Gold_Grillz_Metal.png",
    "Neon": "Gold_Grillz_Neon.png",
    "Tan": "Gold_Grillz_Tan_Brown_Purple_Grey.png",
    "Brown": "Gold_Grillz_Tan_Brown_Purple_Grey.png",
    "Purple": "Gold_Grillz_Tan_Brown_Purple_Grey.png",
    "Grey": "Gold_Grillz_Tan_Brown_Purple_Grey.png"
}

all_images = [] 

METADATA_FILE_NAME = "./metadata/all-traits.json"; 
with open(METADATA_FILE_NAME, "r") as readfile:
    all_images = json.load(readfile)
	
# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

# Get Trait Counts
background_count = {}
for item in backgrounds:
    background_count[item] = 0

clothes_count = {}
for item in clothes:
    clothes_count[item] = 0

earring_count = {}
for item in earrings:
    earring_count[item] = 0

eyes_count = {}
for item in eyewears:
    eyes_count[item] = 0

fur_count = {}
for item in furs:
    fur_count[item] = 0

hat_count = {}
for item in hats:
    hat_count[item] = 0

mouth_count = {}
for item in mouthes:
    mouth_count[item] = 0

for image in all_images:
    background_count[image["Background"]] += 1
    clothes_count[image["Clothes"]] += 1
    earring_count[image["Earring"]] += 1
    eyes_count[image["Eyes"]] += 1
    fur_count[image["Fur"]] += 1
    hat_count[image["Hat"]] += 1
    mouth_count[image["Mouth"]] += 1

#### Generate Images    
for item in all_images:
    print('File Index: ', item["tokenId"])

    background = Image.open(f'./trait-layers/Backgrounds/{background_files[item["Background"]]}').convert("RGBA")
    clothes = Image.open(f'./trait-layers/Clothes/{cloth_files[item["Clothes"]]}').convert("RGBA")
    earring = Image.open(f'./trait-layers/Earrings/{earring_files[item["Earring"]]}').convert("RGBA")
    match item["Eyes"]:
        case "Crossed Out":
            eyes = Image.open(f'./trait-layers/Eyewear/{eyewear_files[item["Eyes"]]}/{eyes_crossed_out_files[item["Fur"]]}').convert("RGBA")
        case 'Tired':
            eyes = Image.open(f'./trait-layers/Eyewear/{eyewear_files[item["Eyes"]]}/{eyes_tired_files[item["Fur"]]}').convert("RGBA")
        case 'Crying':
            eyes = Image.open(f'./trait-layers/Eyewear/{eyewear_files[item["Eyes"]]}/{eyes_crying_files[item["Fur"]]}').convert("RGBA")
        case 'Dollar Sign':
            eyes = Image.open(f'./trait-layers/Eyewear/{eyewear_files[item["Eyes"]]}/{eyes_dollar_sign_files[item["Fur"]]}').convert("RGBA")
        case 'Third Eye':
            eyes = Image.open(f'./trait-layers/Eyewear/{eyewear_files[item["Eyes"]]}/{eyes_third_eye_files[item["Fur"]]}').convert("RGBA")
        case 'Cyclops':
            eyes = Image.open(f'./trait-layers/Eyewear/{eyewear_files[item["Eyes"]]}/{eyes_cyclops_files[item["Fur"]]}').convert("RGBA")
        case 'Kawaii Eyes':
            eyes = Image.open(f'./trait-layers/Eyewear/{eyewear_files[item["Eyes"]]}/{eyes_kawaii_files[item["Fur"]]}').convert("RGBA")
        case 'Primal Eyes':
            eyes = Image.open(f'./trait-layers/Eyewear/{eyewear_files[item["Eyes"]]}/{eyes_primal_files[item["Fur"]]}').convert("RGBA")
        case _:        
            eyes = Image.open(f'./trait-layers/Eyewear/{eyewear_files[item["Eyes"]]}').convert("RGBA") 
    fur = Image.open(f'./trait-layers/Fur/{fur_files[item["Fur"]]}').convert("RGBA")
    hat = Image.open(f'./trait-layers/Hat/{hat_files[item["Hat"]]}').convert("RGBA")
    match item["Mouth"]:
        case "Banana":
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}/{mouth_banana_files[item["Fur"]]}').convert("RGBA")
        case "Biting on knife":
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}/{mouth_Knife_files[item["Fur"]]}').convert("RGBA")
        case "Oh Mouth":
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}/{mouth_OH_files[item["Fur"]]}').convert("RGBA")
        case "Grenade":
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}/{mouth_grenade_files[item["Fur"]]}').convert("RGBA")
        case "Wooden Pipe":
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}/{mouth_wooden_pipe_files[item["Fur"]]}').convert("RGBA")
        case "Toothy Grin":
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}/{mouth_toothy_grin_files[item["Fur"]]}').convert("RGBA")
        case "Silver Grillz":
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}/{mouth_silver_grillz_files[item["Fur"]]}').convert("RGBA")
        case "Pacifier":
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}/{mouth_pacifier_files[item["Fur"]]}').convert("RGBA")
        case "Gold Grillz":
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}/{mouth_gold_grillz_files[item["Fur"]]}').convert("RGBA")
        case _:
            mouth = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}').convert("RGBA")

    #Create each composite
    com1 = Image.alpha_composite(background, fur)
    com2 = Image.alpha_composite(com1, clothes)
    com3 = Image.alpha_composite(com2, earring)
    if item["Hat"] == "Black Durag" or item["Hat"] == "Rainbow Durag":
        if item["Eyes"] == "Night Vision Goggles" or item["Eyes"] == "Scar" or item["Eyes"] == "Third Eye" or item["Eyes"] == "Cyclops":
            com4 = Image.alpha_composite(com3, eyes)
            com5 = Image.alpha_composite(com4, hat)
        else:
            com4 = Image.alpha_composite(com3, hat)
            com5 = Image.alpha_composite(com4, eyes)
        com6 = Image.alpha_composite(com5, mouth)
    else:
        if item["Eyes"] == "Scar" and item["Mouth"] == "Face Mask":
            com4 = Image.alpha_composite(com3, eyes)
            com5 = Image.alpha_composite(com4, mouth)
        else:
            com4 = Image.alpha_composite(com3, mouth)
            com5 = Image.alpha_composite(com4, eyes)
        com6 = Image.alpha_composite(com5, hat)
    
    #Convert to RGB
    rgb_im = com6.convert("RGBA")
    rgb_im = rgb_im.resize((1024, 1024), Image.ANTIALIAS)
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
	
#### Generate Metadata for each Image    
f = open("./metadata/all-traits.json",) 
data = json.load(f)

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

for i in data:
    token_id = i["tokenId"]
    token = {
        "name": f'Gorilla #{token_id + 1}',
        "symbol": "Gorilla",
        "description": "Gorilla Galaxy: Genesis is a collection of 4444 unique, randomly generated Gorillas roaming on the Solana blockchain.",
        "seller_fee_basis_points": 500,
        "image": f'{token_id}.png',
        "external_url": "https://gorillagalaxy.io",
        "attributes": [],
        "collection": {
            "name": "Gorilla Galaxy",
            "family": "GorillaGalaxy"
        },
        "properties": {
            "files": [
                {
                    "uri": f'{token_id}.png',
                    "type": "image/png"
                }
            ],
            "category": "image",
            "creators": [
                {
                    "share": 50,
                    "address": "6rFbybUundKHWwbieyJLwUjAudLEsgJ4ATs22WXmV8i1"
                },
                {
                    "share": 50,
                    "address": "3ipGUMEyrVzbRaq5wQDzX3mtTJptQN21Kbc3aYfxphq8"
                }
            ]
        }
    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Clothes", i["Clothes"]))
    token["attributes"].append(getAttribute("Earring", i["Earring"]))
    token["attributes"].append(getAttribute("Eyes", i["Eyes"]))
    token["attributes"].append(getAttribute("Fur", i["Fur"]))
    token["attributes"].append(getAttribute("Hat", i["Hat"]))
    token["attributes"].append(getAttribute("Mouth", i["Mouth"]))

    with open("./metadata/" + str(token_id) + ".json", "w") as outfile:
        json.dump(token, outfile, indent=4)

f.close()