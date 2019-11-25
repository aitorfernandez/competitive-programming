def three_keyword_suggestions(words, query):
    suggestions = []

    for word in words:
        if query == word[:len(query)]:
            suggestions.append(word)

    suggestions.sort()

    return suggestions[:3]

if __name__ == '__main__':
    words = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad']

    suggestions = three_keyword_suggestions(words, 'mo')
    print(suggestions)
