#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import random

def replace_words(string, percent):

    words = re.findall(r'\b\w+\b', string)
    

    num_replacements = int(len(words) * percent / 100)
    

    replaceable_words = [word for word in words if word.lower() not in {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'is', 'am', 'are', 'was', 'were', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}]
    

    replaced_words = random.sample(replaceable_words, num_replacements)
    new_words = []
    for word in words:
        if word in replaced_words:
            new_words.append("___")
        else:
            new_words.append(word)
    

    return " ".join(new_words)


string = """Headed by the Government Chief Information Officer (GCIO), the Office of the Government Chief Information Officer (OGCIO) is responsible for formulating information technology (IT) strategies, programmes and measures, in addition to providing IT services and support within the Government to help sustain Hong Kong’s position as Asia’s leading digital city."""
percent = 20
new_string = replace_words(string, percent)
print(new_string)


# In[ ]:




