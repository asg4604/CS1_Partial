import linked_code



def convert_to_nodes(dna_string):
    if dna_string[1:] == "":
        return linked_code.LinkNode(dna_string[0], None)
    else:
        return linked_code.LinkNode(dna_string[0], convert_to_nodes(dna_string[1:]))


def is_match(list1, list2):
    if list1.rest == None and list2.rest == None:
        return True
    elif list1.value != list2.value:
        return False
    else:
        return is_match(list1.rest, list2.rest)

def insertion(list1, list2, idx):
    if idx > 0:
        return insertion(list1.rest, list2, idx - 1)
    elif idx == 0:
        return linked_code.concatenate(list2, list1)

def to_string(sequence):
    if sequence == None:
        return ""
    else:
        return str(sequence.value) + to_string(sequence.rest)

list1 = convert_to_nodes("ATCG")
list2 = convert_to_nodes("ATCG")

dna_seq1 = convert_to_nodes("ATCCCG")
dna_seq2 = convert_to_nodes("|GTAA|")




print(to_string(insertion(dna_seq1, dna_seq2, 0)))