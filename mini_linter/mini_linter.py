# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:18:43 2021

@author: =GV=
"""

story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.'

overusedWords = ['really', 'very', 'basically']

unnecessaryWords = ['extremely', 'literally', 'actually']

storyWords = story.split(" ")

betterWords = [word for word in storyWords if word not in unnecessaryWords]

def overusedCount(overusedWords, words):
    wordCount = {word:0 for word in overusedWords}
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
    return [(word, count) for word, count in wordCount.items()]

overusedWordCount = overusedCount(overusedWords, betterWords)
sentences = [result for sentence in story.split('.') for result in sentence.split('!') if not result == '']

def mostUsedWord(words):
    result = 0
    mostusedWord = ''
    uniqueWords = list(set([word.strip('\'-,.!?()"').lower() for word in words if not word == '']))
    for uniqueWord in uniqueWords:
        count = 0
        for word in words:
            if word == uniqueWord:
                count += 1
        if count > result:
            result = count
            mostusedWord = uniqueWord
            
    return f'Most used word is "{mostusedWord}", used a total of {result} times'

    
print(f'Word count = {len(betterWords)}\nSentence count = {len(sentences)}\n')
for word, count in overusedWordCount:
    print(f'"{word}" ={count}')

print()
print(mostUsedWord(betterWords))

