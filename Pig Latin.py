def translate(text):
    translated_words = []
    words = text.split()
    suffix = 'ay'
    if len(words) > 1:
        for word in words:
            translated_words.append(translate(word))
        return ' '.join(translated_words)
    else:
        word = words[0]
        vowels = 'aeiou'
        #add more
        clusters = ['ch','squ','qu','thr','th','sch','rh']
        edge_cases = ['xr','yt']
        if word[0] in vowels:
            return word+suffix
        else:
            for cluster in clusters:
                if word.startswith(cluster):
                    return word[len(cluster):]+cluster+suffix
            for case in edge_cases:
                if word.startswith(case):
                    return word+suffix
            else:
                return word[1:]+word[0]+suffix