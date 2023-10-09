import tokenize

target_file_lists = ["second.py"]
corpus_file_lists = ["third.py", "hello.py"]


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

# tokenize the corpus:
token_list_corpus = tokenize_to_set(corpus_file_lists)


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

print(target_2_grams)
print(corpus_2_grams)

# compare the to find the redundant
repeat = 0
for list_1 in target_2_grams:
    for list_2 in corpus_2_grams:
        if list_1 == list_2:
            repeat += 1
            break

redundant = (repeat + 1) / len(token_list_target)
print(redundant)


def tokenize_into_3_grams(token_list):
    list_3_grams = []

    for i in range(len(token_list) - 2):
        list_3_grams.append(token_list[i : i + 3])

    return list_3_grams


# ngrams the list of tokenize target project
target_3_grams = tokenize_into_3_grams(token_list_target)
# ngrams the list of tokenize corpus
corpus_3_grams = tokenize_into_3_grams(token_list_corpus)

print(target_3_grams)
print(corpus_3_grams)

# compare the to find the redundant
repeat = 0
for list_1 in target_3_grams:
    for list_2 in corpus_3_grams:
        if list_1 == list_2:
            repeat += 1
            break

redundant = (repeat + 2) / len(token_list_target)
print(redundant)
