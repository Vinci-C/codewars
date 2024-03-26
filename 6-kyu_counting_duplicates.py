def duplicate_count(text):
    count = 0
    text = text.lower()
    text_dict = {i:text.count(i) for i in text}
    for value in text_dict:
        if text_dict[value] > 1: count += 1
    return count
