from collections import defaultdict

def pattern(word):
    """
    Take a word and return its pattern.
    For example HELLO would be ABCCD
    """
    alphabet = [chr(i) for i in range(ord('A'),ord('Z'))]
    word_dict = {}
    pattern = ""
    for i in word:
        if i in word_dict:
            pass
        else:
            word_dict[i] = alphabet.pop(0)

    for i in word:
        pattern += word_dict[i]

    return pattern

def filter_list(cipher_word, word_choice, alpha_dict):
    """
    Filter List
    Tell us wether the word choice could possibly be the cipher word.
    """
    for i in range(len(cipher_word)):
        if word_choice[i] not in alpha_dict[cipher_word[i]]:
            return False
    return True

def eliminate_choices(word_choices, alpha_dict):
    """
    Eliminate choices, that have letters in positions that don't make sense.
    """
    for cipher_word in word_choices:
        word_list = word_choices[cipher_word]
        filtered_list = [word for word in word_list if filter_list(cipher_word, word, alpha_dict)]
        word_choices[cipher_word] = filtered_list
        if len(filtered_list) != 0:
            for i in range(len(cipher_word)):
                letter_list = []
                for word in filtered_list:
                    letter_list.append(word[i])

                alpha_dict[cipher_word[i]] = alpha_dict[cipher_word[i]].intersection(set(letter_list))

    return alpha_dict

def propagate(alpha_dict):
    """
    If we have a letter down to one possibility remove it from the others
    """
    for i in alpha_dict:
        if len(alpha_dict[i]) == 1:
            correct_letter = alpha_dict[i].copy()
            correct_letter = correct_letter.pop()
            for j in alpha_dict:
                if j != i and len(alpha_dict[j]) != 1:
                    alpha_dict[j].discard(correct_letter)
    return alpha_dict

def filter_word_list_by_length(ciphertext):
    """
    Return list of words that are the lengths of the words in the ciphertext
    """
    word_lengths = {}
    word_bank = []
    for word in  ciphertext.split(" "):
        word_lengths[len(word)] = ""

    word_list = open("words", 'r')
    for i in word_list:
        if len(i.rstrip()) in word_lengths:
            word_bank.append(i.rstrip().upper())

    return word_bank

def generate_new_dict(puzzle):
    for character in puzzle.replace(' ',''):
        alphabet = [chr(i) for i in range(ord('A'),ord('Z') + 1)]
        alpha_dict[character] = set(alphabet)
        alpha_dict[character].discard(character)
    return alpha_dict

def get_possible_words(puzzle):
    word_bank = filter_word_list_by_length(puzzle)
    patterned_cipher = {}
    word_choices = {}
    cipher_dict = {}


    for cipher_word in puzzle.split(' '):
        patterned_cipher[pattern(cipher_word)] = []
        cipher_dict[cipher_word] = pattern(cipher_word)

    for word in word_bank:
        if pattern(word) in patterned_cipher:
            patterned_cipher[pattern(word)].append(word)

    for key in cipher_dict:
        word_choices[key] = patterned_cipher[pattern(key)]

    return word_choices



if __name__ == "__main__":

    alpha_dict = {}

    puzzle = "TGIAB FZU TGPHVGHPB FPB GSB BTTBZVB QR F CQQW OPBFG KUBFT FPB SQOLFTS"


    #Generate a clean alphabet dictionary
    alpha_dict = generate_new_dict(puzzle)
    #Get associated with their patterns
    word_bank = get_possible_words(puzzle)

    for i in range(10):
        alpha_dict = eliminate_choices(word_bank,alpha_dict)
        alpha_dict = propagate(alpha_dict)

    solved = ""
    for i in puzzle:
        if i != ' ':
            solved += str(list(alpha_dict[i]))
        else:
            solved += ' '

    print solved
