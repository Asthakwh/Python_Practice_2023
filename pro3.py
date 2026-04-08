import re
def match_txt(txt_data):
    pattern='ab'#{4,8} in bracket
    if re.search(pattern, txt_data):
        return ('matchfound')
    else:
        return ('match not found')
print(match_txt("abc"))
print(match_txt("aabbbc"))
print(match_txt("aaaa"))
print(match_txt("ab"))
print(match_txt("aabb"))
print(match_txt("dfdj"))
print(match_txt("cc"))



