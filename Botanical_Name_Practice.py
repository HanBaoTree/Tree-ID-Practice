import random

# Updated tree groups with botanical names based on the provided file.
tree_groups = {
    "Group 1": [
        {"botanical": "Betula pendula", "common": "Silver Birch"},
        {"botanical": "Betula papyrifera", "common": "Paper Birch"},
        {"botanical": "Betula alleghaniensis", "common": "Yellow Birch"},
        {"botanical": "Betula nigra", "common": "River Birch"},
        {"botanical": "Alnus glutinosa", "common": "Black Alder"},
        {"botanical": "Carpinus caroliniana", "common": "American Hornbeam"},
        {"botanical": "Ostrya virginiana", "common": "Eastern Hophornbeam"},
        {"botanical": "Corylus colurna", "common": "Turkish Hazel"}
    ],
    "Group 2": [
        {"botanical": "Gleditsia triacanthos", "common": "Honey Locust"},
        {"botanical": "Gymnocladus dioicus", "common": "Kentucky Coffeetree"},
        {"botanical": "Robinia pseudoacacia", "common": "Black Locust"},
        {"botanical": "Cercis canadensis", "common": "Eastern Redbud"},
        {"botanical": "Celtis occidentalis", "common": "Common Hackberry"},
        {"botanical": "Ginkgo biloba", "common": "Ginkgo"},
        {"botanical": "Ailanthus altissima", "common": "Tree of Heaven"},
        {"botanical": "Sorbus americana", "common": "American Mountain Ash"}
    ],
    "Group 3": [
        {"botanical": "Platanus occidentalis", "common": "American Sycamore"},
        {"botanical": "Platanus x acerifolia", "common": "London Plane"},
        {"botanical": "Tilia cordata", "common": "Littleleaf Linden"},
        {"botanical": "Tilia americana", "common": "American Linden"},
        {"botanical": "Liriodendron tulipifera", "common": "Tulip Tree"},
        {"botanical": "Magnolia acuminata", "common": "Cucumber Magnolia"},
        {"botanical": "Liquidambar styraciflua", "common": "Sweetgum"},
        {"botanical": "Salix fragilis", "common": "Crack Willow"}
    ],
    "Group 4": [
        {"botanical": "Amelanchier arborea", "common": "Downy Serviceberry"},
        {"botanical": "Crataegus spp.", "common": "Hawthorn"},
        {"botanical": "Malus spp.", "common": "Apple"},
        {"botanical": "Prunus pensylvanica", "common": "Pin Cherry"},
        {"botanical": "Prunus serotina", "common": "Black Cherry"},
        {"botanical": "Prunus virginiana", "common": "Chokecherry"},
        {"botanical": "Pyrus calleryana 'Chanticleer'", "common": "Callery Pear"}
    ],
    "Group 5": [
        {"botanical": "Aralia elata", "common": "Japanese Angelica Tree"},
        {"botanical": "Elaeagnus angustifolia", "common": "Russian Olive"},
        {"botanical": "Rhamnus cathartica", "common": "Common Buckthorn"},
        {"botanical": "Rhus typhina", "common": "Staghorn Sumac"},
        {"botanical": "Nyssa sylvatica", "common": "Black Tupelo"},
        {"botanical": "Morus alba", "common": "White Mulberry"},
        {"botanical": "Morus rubra", "common": "Red Mulberry"}
    ],
    "Group 6": [
        {"botanical": "Populus alba", "common": "White Poplar"},
        {"botanical": "Populus balsamifera", "common": "Balsam Poplar"},
        {"botanical": "Populus x canadensis", "common": "Hybrid Poplar"},
        {"botanical": "Populus grandidentata", "common": "Bigtooth Aspen"},
        {"botanical": "Populus nigra 'Italica'", "common": "Lombardy Poplar"},
        {"botanical": "Populus tremuloides", "common": "Quaking Aspen"},
        {"botanical": "Salix alba 'Tristis'", "common": "Golden Weeping Willow"}
    ],
    "Group 7": [
        {"botanical": "Ulmus americana", "common": "American Elm"},
        {"botanical": "Ulmus glabra", "common": "Wych Elm"},
        {"botanical": "Ulmus procera", "common": "English Elm"},
        {"botanical": "Ulmus pumila", "common": "Siberian Elm"},
        {"botanical": "Ulmus rubra", "common": "Slippery Elm"}
    ]
}

def select_groups():
    print("Available groups:")
    for group in tree_groups.keys():
        print(f"- {group}")

    selected = input("Enter the group numbers to practice (comma-separated) or 'all' for all groups: ").strip()
    if selected.lower() == 'all':
        return list(tree_groups.keys())
    else:
        selected_groups = [f"Group {num.strip()}" for num in selected.split(',') if f"Group {num.strip()}" in tree_groups]
        if not selected_groups:
            print("Invalid selection. Defaulting to all groups.")
            return list(tree_groups.keys())
        return selected_groups

def practice_flashcards(selected_groups):
    questions = [
        (tree["common"], tree["botanical"]) 
        for group in selected_groups for tree in tree_groups[group]
    ]
    random.shuffle(questions)

    for common_name, botanical_name in questions:
        user_answer = input(f"What is the botanical name for '{common_name}'? ").strip()
        if user_answer.lower() == botanical_name.lower():
            print("Correct!\n")
        else:
            print(f"Oops! The correct answer is '{botanical_name}'.\n")

def main():
    print("Welcome to the Botanical Name Flashcards!")
    selected_groups = select_groups()
    practice_flashcards(selected_groups)

if __name__ == "__main__":
    main()
