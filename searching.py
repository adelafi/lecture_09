import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]


def linear_search(data, number):
    summation = 0
    number_idxs = []
    for i, num in enumerate(data):
        if num == number:
            number_idxs.append(i)
            summation += 1
    number_count = {"Positions": number_idxs, "Count": summation}
    return number_count


def pattern_search(sequence, template):
    index = set()
    for i, letter in enumerate(sequence):
        part = sequence[i:i+len(template)]
        if part == template:
            index.add(i)
    return index


def binary_search(sequence, number):
    length = len(sequence)
    while length > 0:
        length = len(sequence)
        if length % 2 == 0:
            middle_idx = int(length / 2)
        else:
            middle_idx = int(length / 2 - 0.5)
        if sequence[middle_idx] == number:
            return middle_idx
        else:
            if sequence[middle_idx] < number:
               search = sequence[middle_idx:]
            else:
               search = sequence[:middle_idx]
        for i, num in enumerate(search):
            if num == number:
                return i
        return None
def main():
    sequential_data = read_data("sequential.json", "dna_sequence")
    print(sequential_data)
    print(pattern_search(sequential_data, template))
    linear_data = read_data("sequential.json", "unordered_numbers")
    print(linear_data)
    print(linear_search(linear_data, number))
    ordered_numbers = read_data("sequential.json", "ordered_numbers")
    print(ordered_numbers)
    print(binary_search(ordered_numbers, bin_num))

if __name__ == '__main__':
    number = 9
    bin_num = 22
    template = "ATA"
    main()
