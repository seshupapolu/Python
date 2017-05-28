from urllib.request import urlopen
with urlopen("http://sixty-north.com/c/t.txt") as story:
    story_words=[]
    for line in story:
        line_word=line.decode('utf-8').split()
        for word in line_word:
            story_words.append(word)

print(story_words)