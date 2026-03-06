
def findAndReplace(text, oldText, newText):
    i = 0
    replacedText = ''
    textSize = len(text)
    oldTextSize = len(oldText)
    while i < textSize:
        if text[i:(i+oldTextSize)] == oldText:
            replacedText += newText
            i += oldTextSize
        else:
            replacedText += text[i]
            i += 1

    return replacedText


assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
