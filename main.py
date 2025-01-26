def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_character_dict = count_character_appearance(file_contents)
        count_character_list = convert_count_character_appearance_dict_to_list(count_character_dict)
        pretty_print(count_character_list)


# return number (integer)
def count_word(words):
    return len(words.split())

# return dictionary
def count_character_appearance(words):
    count_character_dict = {}

    for character in words:
        character = character.lower()

        if character not in count_character_dict:
            count_character_dict[character] = 1
        else:
            count_character_dict[character] += 1

    return count_character_dict

def sort_on(dict):
    return dict["count"]

def convert_count_character_appearance_dict_to_list(count_character_dict):
    count_character_appearance_list = []

    for character in count_character_dict:
        if character.isalpha():
            character_dict = {}
            character_dict["character"] = character
            character_dict["count"] = count_character_dict[character]
            count_character_appearance_list.append(character_dict)

    count_character_appearance_list.sort(reverse=True, key=sort_on)
    return count_character_appearance_list

def pretty_print(count_character_list):
    for character_dict in count_character_list:
        print(f"The '{character_dict["character"]}' character was found {character_dict["count"]} times")

main()
