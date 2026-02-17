# List of seasons with advice
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

# List of plant types with advice
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


def get_advice(data_list, key, user_input):
    """
    Search a list of dictionaries for a matching value for either the season
    or plant_type and return its advice.

    Parameters:
        data_list (list): List of dictionaries containing season,
        plant_type and advice data.
        key (str): Key that decides which data list to check
        (e.g., 'season' or 'plant_type').
        user_input (str): The users' input.

    Returns:
        str: The advice string for the matched item, or an empty string
        if no match.
    """
    for item in data_list:
        if item[key].lower() == user_input.lower():
            return item["advice"] + " "
    return ""


def print_advice():
    """
    Prompt the user for a season and plant type, then print the
    combined advice.

    If no matching advice is found for either input, a default message
    is displayed.
    """
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
