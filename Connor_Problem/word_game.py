import itertools
ENGLISH_FILE = "american_english.txt"
def sort_word(word):
   sorted_chars = sorted(word)
   sorted_word = ""
   for char in sorted_chars:
        sorted_word += char
   return char

def build_dictionary():
    english_dict = {}
    for line in open(ENGLISH_FILE):
        line = line.strip()
        sorted_word = line
        if sorted_word not in english_dict:
            english_dict[sorted_word] = [line]
        else:
            english_dict[sorted_word].append(line)

    return english_dict

def assemble_list_from_permutations(permutations):
    words = []
    for char_tuple in permutations:
        word = ""
        for char in char_tuple:
            word += char
        words.append(word)
    return words

def quick_lookup(dictionary, word):
    sorted_word = sort_word(word)
    if sorted_word not in dictionary.keys():
        return False
    else:
        return word in dictionary[sorted_word]
def main():
    # letters_given = input("Letters Given: ")
    # size_of_word = int(input("Word Size: "))
    english_dict = build_dictionary()
    letters_given = "aiteondme"
    size_of_word = 4
    letter_set = list(letters_given)
    permutations = list(itertools.permutations(letter_set, size_of_word))
    possible_outputs = assemble_list_from_permutations( permutations )
    print(possible_outputs)
    real_options = list(filter(lambda word: quick_lookup(english_dict, word), possible_outputs))
    print(real_options)

main()
    


