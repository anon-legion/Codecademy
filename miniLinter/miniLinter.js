let story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.'

let overusedWords = ['really', 'very', 'basically']

let unnecessaryWords = ['extremely', 'literally', 'actually']

let storyWords = story.split(" ")

let betterWords = storyWords.filter(word => {
    if (unnecessaryWords.includes(word)) {
        return false
    } else {
        return true
    }
})

let count1 = 0
let count2 = 0
let count3 = 0

betterWords.forEach(word => {
    switch (word) {
        case overusedWords[0]:
            count1++
            break

        case overusedWords[1]:
            count2++
            break

        case overusedWords[2]:
            count3++
            break
    }
})


let sentenceCount = 0
betterWords.forEach(word => {
    if (word[word.length - 1] === '.' || word[word.length - 1] === '!') {
        sentenceCount++
    }
})


const logCount = (storyWords, sentenceCount, overUsed1, overUsed2, overUsed3) => {
    console.log(`Word count = ${storyWords.length}\nSentence count = ${sentenceCount}\n"${overusedWords[0]}" count = ${overUsed1}\n"${overusedWords[1]}" count = ${overUsed2}\n"${overusedWords[2]}" count = ${overUsed3}\n`)
}



function wordCount(words) {
    let result = 0
    let mostUsedWord = ''
    let uniqueWords = []
    words.forEach(word => {
        if (uniqueWords.indexOf(word.toLowerCase()) === -1) {
            uniqueWords.push(word.toLowerCase())
        }
    })
    uniqueWords.forEach(uniqueWord => {
        let count = 0
        words.forEach(word => {
            if (word === uniqueWord) {
                count++
            }
        })
        if (count > result) {
            result = count
            mostUsedWord = uniqueWord
        }
    })
    return `Most used word is "${mostUsedWord}", used a total of ${result} times`
}

logCount(betterWords, sentenceCount, count1, count2, count3)
console.log(betterWords.join(' '))
console.log()
console.log(wordCount(betterWords) + '\n')