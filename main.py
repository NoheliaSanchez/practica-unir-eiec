"""
License: Apache
Organization: UNIR
Student: Nohelia Sánchez
"""

import os
import sys
import argparse

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER = 'ascendente'

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    return sorted(items, reverse=not ascending)

def remove_duplicates_from_list(items):
    return list(set(items))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort a list of words.')
    parser.add_argument('filename', type=str, help='Input file with words.')
    parser.add_argument('--orden', choices=['ascendente', 'descendente'], default=DEFAULT_ORDER, help='Sort order (ascending or descending).')
    parser.add_argument('--eliminar-duplicados', action='store_true', help='Remove duplicate words.')

    args = parser.parse_args()
    
    filename = args.filename
    remove_duplicates = args.eliminar_duplicados
    ascending = (args.orden == 'ascendente')

    print(f"Processing file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist.")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    sorted_words = sort_list(word_list, ascending=ascending)
    print(sorted_words)
