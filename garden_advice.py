season_data = [
    {
        "season": "summer",
        "advice": "Water your plants regularly and provide some shade."
    },
    {
        "season": "winter",
        "advice": "Protect your plants from frost with covers."
    },
    {
        "season": "spring",
        "advice": "Start planting seeds and prune old growth."
    },
    {
        "season": "autumn",
        "advice": "Harvest mature crops and prepare soil for winter."
    },
    {
        "season": "dry",
        "advice": "Water deeply but less frequently to retain moisture."
     },
    {
        "season": "none",
        "advice": "No advice for this season."
    }
]

plant_data = [
    {
        "plant_type": "Flower",
        "advice": "Use fertiliser to encourage blooms."
    },
    {
        "plant_type": "Vegetable",
        "advice": "Keep an eye out for pests!"
    },
    {
        "plant_type": "herb",
        "advice": "Harvest leaves regularly for better growth."
    },
    {
        "plant_type": "succulent",
        "advice": "Avoid overwatering and provide bright light."
    },
    {
        "plant_type": "tree",
        "advice": "Prune dead branches and mulch the base."
    },
    {
        "plant_type": "fruit",
        "advice": "Protect fruits from birds and insects."
    },
    {
        "plant_type": "none",
        "advice": "No advice for this type of plant."
    }
]

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.


def get_advice(data_list, key, user_input):
    for item in data_list:
        if item[key].lower() == user_input.lower():
            return item["advice"] + " "
    return ""


def print_advice():
    season_input = input("Season: ")
    plant_type_input = input("Plant type: ")
    season_advice = get_advice(season_data, "season", season_input)
    plant_advice = get_advice(plant_data, "plant_type", plant_type_input)

    if not season_advice:
        season_advice = "No advice for the given season. "

    if not plant_advice:
        plant_advice = "No advice for the given plant type. "

    print(season_advice + plant_advice)


print_advice()