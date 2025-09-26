def word_occurrence_count():
    words = input().split()
    word_count = {}
    result = []
    for word in words:
        result.append(word_count.get(word, 0))
        word_count[word] = word_count.get(word, 0) + 1
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    word_occurrence_count()