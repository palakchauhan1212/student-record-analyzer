def changing_paragraph(paragraph):
    punctuation = '!+-,._@^*'
    clear_text = ''
    for char in paragraph.lower():
        if char not in punctuation:
            clear_text  += char
    return clear_text

def analyze_text(paragraph):
    words = changing_paragraph(paragraph).split()
    frequency = {}
    unique_words = set()
    for word in words:
        unique_words.add(word)
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    # max based on values(frequency) (char[1]) | max based on key(alphabets) (char[0])
    most_repeated_word = max(frequency.items(), key = lambda char: char[1])
    return {"frequency":frequency,"unique words":unique_words,"most repeated word":most_repeated_word}

def display_text(result):
    print('Frequency of each word:',result['frequency'])
    print(f"Most repeated word:{result['most repeated word'][0]} {result['most repeated word'][1]}times")
    print('Set of unique words:',result['unique words'])

def main():
    paragraph = input('Enter the Paragraph:')
    result = analyze_text(paragraph)    
    display_text(result)
main()