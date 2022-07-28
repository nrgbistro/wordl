
# Filter bad words out of list of all English words
with open('all_english_words.txt') as text,  open('bad_words_filter.txt') as filter:
    st = set(filterWord.lower() for filterWord in filter)
    txt = set(textWord.lower() for textWord in text)
    englishNoSwearing = [word for word in txt if word not in st]

# Convert common words txt to list (and remove duplicates if any)
with open('most_common_words_no_swear.txt') as commonWords:
    st = set(commonWord.lower() for commonWord in commonWords)
    mostCommon = [word for word in st]

# Filter out words that aren't 4-8 letters long
for word in englishNoSwearing:
    if (word.len() < 4 or word.len() > 8):
        englishNoSwearing.remove()

for words in mostCommon:
    if (words.len() < 4 or words.len() > 8):
        mostCommon.remove()