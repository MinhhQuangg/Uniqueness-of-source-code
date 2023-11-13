import tokenize
import os
import subprocess


# Get the root of python file from the folder
def get_python_files(folder_path):
    python_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files


# target folder path
target_folder_path = r"C:\Users\minhq\Desktop\target"
# corpus folder path
corpus_folder_path = r"C:\Users\minhq\Desktop\corpus"

# target file lists
target_file_lists = get_python_files(target_folder_path)

# corpus file lists
corpus_file_lists = get_python_files(corpus_folder_path)
# print(target_file_lists)
# print(corpus_file_lists)


# Tokenize function
def tokenize_to_set(file_lists):
    all_tokens = []

    for file in file_lists:
        with tokenize.open(file) as file:
            tokens = tokenize.generate_tokens(file.readline)

            token_list = []

            for token in tokens:
                token_list.append(token[1])

        token_list = token_list[:-2]
        all_tokens.extend(token_list)

    return all_tokens


# tokenize the target project:
token_list_target = tokenize_to_set(target_file_lists)
# print(token_list_target)

# tokenize the corpus:
token_list_corpus = tokenize_to_set(corpus_file_lists)
# print(token_list_corpus)


# 2-gram function
def tokenize_into_2_grams(token_list):
    list_2_grams = []

    for i in range(len(token_list) - 1):
        list_2_grams.append(token_list[i : i + 2])

    return list_2_grams


# ngrams the list of tokenize target project
target_2_grams = tokenize_into_2_grams(token_list_target)
# ngrams the list of tokenize corpus
corpus_2_grams = tokenize_into_2_grams(token_list_corpus)

# print(target_2_grams)
# print(corpus_2_grams)

# compare the to find the redundant
repeat = 0
for list_1 in target_2_grams:
    for list_2 in corpus_2_grams:
        if list_1 == list_2:
            repeat += 1
            break

redundant_2_grams = (repeat + 1) / len(token_list_target)
print(redundant_2_grams)


def tokenize_into_3_grams(token_list):
    list_3_grams = []

    for i in range(len(token_list) - 2):
        list_3_grams.append(token_list[i : i + 3])

    return list_3_grams


# ngrams the list of tokenize target project
target_3_grams = tokenize_into_3_grams(token_list_target)
# ngrams the list of tokenize corpus
corpus_3_grams = tokenize_into_3_grams(token_list_corpus)

# print(target_3_grams)
# print(corpus_3_grams)

# compare the to find the redundant
repeat = 0
for list_1 in target_3_grams:
    for list_2 in corpus_3_grams:
        if list_1 == list_2:
            repeat += 1
            break

redundant_3_grams = (repeat + 2) / len(token_list_target)
print(redundant_3_grams)


# 5-gram function
def tokenize_into_5_grams(token_list):
    list_5_grams = []

    for i in range(len(token_list) - 4):
        list_5_grams.append(token_list[i : i + 5])

    return list_5_grams


# ngrams the list of tokenize target project
target_5_grams = tokenize_into_5_grams(token_list_target)
# ngrams the list of tokenize corpus
corpus_5_grams = tokenize_into_5_grams(token_list_corpus)

# print(target_5_grams)
# print(corpus_5_grams)

# compare the to find the redundant
repeat = 0
for list_1 in target_5_grams:
    for list_2 in corpus_5_grams:
        if list_1 == list_2:
            repeat += 1
            break

redundant_5_grams = (repeat + 4) / len(token_list_target)
print(redundant_5_grams)


# 10-gram function
def tokenize_into_10_grams(token_list):
    list_10_grams = []

    for i in range(len(token_list) - 9):
        list_10_grams.append(token_list[i : i + 10])

    return list_10_grams


# ngrams the list of tokenize target project
target_10_grams = tokenize_into_10_grams(token_list_target)
# ngrams the list of tokenize corpus
corpus_10_grams = tokenize_into_10_grams(token_list_corpus)

# print(target_10_grams)
# print(corpus_10_grams)

# compare the to find the redundant
repeat = 0
for list_1 in target_10_grams:
    for list_2 in corpus_10_grams:
        if list_1 == list_2:
            repeat += 1
            break

redundant_10_grams = (repeat + 9) / len(token_list_target)
print(redundant_10_grams)
