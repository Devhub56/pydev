#!/usr/bin/env python
import re
some_random_text = 'alpha, beta,,,,gamma    delta'
b=re.split('[, ]+', some_random_text)# you can add the maximum number of splits allowed.(maxsplit=n), where n is an integer
print(b)

#testing the findall

some_parameters = '[a-zA-Z]+'
other_parameters = r'[.?\-",]+'
text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
d=re.findall(some_parameters, text)
ef=re.findall(other_parameters,text)

print(d,ef)
#sub (Replaces left most occurance of a pattern)
pat = '{name}'
text = 'Dear {name}...'
subbed=re.sub(pat, 'Mr. Gumby', text)
print (subbed)

emphasis_pattern = re.compile(r'''
... \*               # Beginning emphasis tag -- an asterisk
... (                # Begin group for capturing phrase
... [^\*]+           # Capture anything except asterisks
... )                # End group
... \*               # Ending emphasis tag
...            ''', re.VERBOSE)
s=re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!')
print (s)
