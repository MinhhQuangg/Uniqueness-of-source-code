import tokenize
import os


# Get the root of python file from the folder
def get_python_files(folder_path):
    python_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files


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
token_list_target = tokenize_to_set(get_python_files(r"C:\Users\minhq\Desktop\target"))

# tokenize the corpus:
token_list_corpus = tokenize_to_set(get_python_files(r"C:\Users\minhq\Desktop\corpus"))


def tokenize_into_n_grams(token_list, n):
    list_n_grams = []

    for i in range(len(token_list) - 1):
        list_n_grams.append(token_list[i : i + n])

    return list_n_grams


def syntacticRedundant(n):
    if n <= len(token_list_target):
        target_grams = tokenize_into_n_grams(token_list_target, n)
        corpus_grams = tokenize_into_n_grams(token_list_corpus, n)
        repeat = 0
        for list_1 in target_grams:
            for list_2 in corpus_grams:
                if list_1 == list_2:
                    repeat += 1
                    break
        if repeat == 0:
            redundant = 0
        else:
            redundant = (repeat + n - 1) / len(token_list_target)
    return redundant


for i in range(23, 24):
    print(syntacticRedundant(i))
