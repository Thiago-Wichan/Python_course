# E X E R C I S E # 1 0 : F I N D A N D R E P L A C E


def findAndReplace(text: str, oldText: str, newText: str):
    replaceText = ''
    i = 0
    while i < len(text):
        if text[i:i + len(oldText)] == oldText:
            replaceText += newText
            i += len(oldText)
        else:
            replaceText += text[i]
            i += 1
    return replaceText


assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
