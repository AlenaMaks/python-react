# 2 задание

def is_palindrome(text):
    text = text.lower()
    for w in text:
        if not(w.isalpha()):
            text = text.replace(w, '')
    if text == '':
        raise ValueError('Нет текстовых символов для проверки.')
    for i in range(1, (len(text)//2)+1):
        if not(text[i-1] == text[-i]):
            return False
    return True

assert is_palindrome('П& 1%упg%') == False
assert is_palindrome('П& 1%уп%') == True
assert is_palindrome('3456 g 5678') == True

try:
    is_palindrome('')
except ValueError as e:
    assert str(e) == 'Нет текстовых символов для проверки.'

try:
    is_palindrome('123_ %6)( !!1)')
except ValueError as e:
    assert str(e) == 'Нет текстовых символов для проверки.'
    
assert is_palindrome('кК') == True
assert is_palindrome('кг') == False
assert is_palindrome("Лёша на полке клопа нашёл") == True