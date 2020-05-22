```python
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
bat
mat
cat
'''
sentence = 'Start a sentence and then bring it to an end seNtEnce sEnteNce SentenCe '

```


```python
def pat_iter(pattern_to_find, text):
    pattern = re.compile(pattern_to_find)
    # finditer iterates through all the matches
    matches = pattern.finditer(text)
    for match in matches:
        print(match)
```


```python
# search a .
pat_iter(r'\.', text_to_search)
```

    <re.Match object; span=(111, 112), match='.'>
    <re.Match object; span=(146, 147), match='.'>
    <re.Match object; span=(167, 168), match='.'>
    <re.Match object; span=(171, 172), match='.'>
    <re.Match object; span=(218, 219), match='.'>
    <re.Match object; span=(249, 250), match='.'>
    <re.Match object; span=(262, 263), match='.'>
    


```python
# \b for word boundary
pat_iter(r'\bHa', text_to_search)
```

    <re.Match object; span=(66, 68), match='Ha'>
    <re.Match object; span=(69, 71), match='Ha'>
    


```python
# \B for NOT word boundary
pat_iter(r'\BHa', text_to_search)
```

    <re.Match object; span=(71, 73), match='Ha'>
    


```python
# match phone number pattern 
pat_iter(r'\d\d\d.\d\d\d.\d\d\d\d', text_to_search)
```

    <re.Match object; span=(151, 163), match='321-555-4321'>
    <re.Match object; span=(164, 176), match='123.555.1234'>
    <re.Match object; span=(177, 189), match='123*555*1234'>
    <re.Match object; span=(190, 202), match='800-555-1234'>
    <re.Match object; span=(203, 215), match='900-555-1234'>
    


```python
# open test_data file 
with open('test_data.txt') as f:
    file_data = f.read()
```


```python
pat_iter(r'\d\d\d.\d\d\d.\d\d\d\d', file_data)
```

    <re.Match object; span=(12, 24), match='615-555-7164'>
    <re.Match object; span=(102, 114), match='800-555-5669'>
    <re.Match object; span=(191, 203), match='560-555-5153'>
    <re.Match object; span=(281, 293), match='900-555-9340'>
    <re.Match object; span=(378, 390), match='714-555-7405'>
    <re.Match object; span=(467, 479), match='800-555-6771'>
    <re.Match object; span=(557, 569), match='783-555-4799'>
    <re.Match object; span=(647, 659), match='516-555-4615'>
    <re.Match object; span=(740, 752), match='127-555-1867'>
    <re.Match object; span=(831, 843), match='608-555-4938'>
                               ...
    <re.Match object; span=(7872, 7884), match='800-555-1372'>
    <re.Match object; span=(7961, 7973), match='300-555-7821'>
    <re.Match object; span=(8051, 8063), match='133-555-3889'>
    <re.Match object; span=(8139, 8151), match='705-555-6863'>
    <re.Match object; span=(8228, 8240), match='215-555-9449'>
    <re.Match object; span=(8319, 8331), match='988-555-6112'>
    <re.Match object; span=(8405, 8417), match='623-555-3006'>
    <re.Match object; span=(8489, 8501), match='192-555-4977'>
    <re.Match object; span=(8574, 8586), match='178-555-4899'>
    <re.Match object; span=(8658, 8670), match='952-555-3089'>
    <re.Match object; span=(8751, 8763), match='900-555-6426'>
    


```python
# matching phone number with only . or -
# using character set []
pat_iter(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d', text_to_search)
```

    <re.Match object; span=(151, 163), match='321-555-4321'>
    <re.Match object; span=(164, 176), match='123.555.1234'>
    <re.Match object; span=(190, 202), match='800-555-1234'>
    <re.Match object; span=(203, 215), match='900-555-1234'>
    


```python
# match numbers with starting with only 800 or 900
pat_iter(r'[89]00[.-]\d\d\d[.-]\d\d\d\d', text_to_search)
```

    <re.Match object; span=(190, 202), match='800-555-1234'>
    <re.Match object; span=(203, 215), match='900-555-1234'>
    


```python
# match every character not in charset using ^
pat_iter(r'[^a-zA-Z]', text_to_search)
```

    <re.Match object; span=(0, 1), match='\n'>
    <re.Match object; span=(27, 28), match='\n'>
    <re.Match object; span=(54, 55), match='\n'>
    <re.Match object; span=(55, 56), match='1'>
    <re.Match object; span=(56, 57), match='2'>
    <re.Match object; span=(57, 58), match='3'>
    <re.Match object; span=(58, 59), match='4'>
    <re.Match object; span=(59, 60), match='5'>
    <re.Match object; span=(60, 61), match='6'>
    <re.Match object; span=(61, 62), match='7'>
                               ...
    <re.Match object; span=(245, 246), match='\n'>
    <re.Match object; span=(249, 250), match='.'>
    <re.Match object; span=(250, 251), match=' '>
    <re.Match object; span=(259, 260), match='\n'>
    <re.Match object; span=(262, 263), match='.'>
    <re.Match object; span=(263, 264), match=' '>
    <re.Match object; span=(265, 266), match='\n'>
    <re.Match object; span=(269, 270), match='\n'>
    <re.Match object; span=(273, 274), match='\n'>
    <re.Match object; span=(277, 278), match='\n'>
    


```python
# match every 3 character word except bat
pat_iter(r'[^b]at', text_to_search)
```

    <re.Match object; span=(270, 273), match='mat'>
    <re.Match object; span=(274, 277), match='cat'>
    


```python
# quantifier
pat_iter(r'\d{3}[.-]\d{3}[.-]\d{4}', text_to_search)
```

    <re.Match object; span=(151, 163), match='321-555-4321'>
    <re.Match object; span=(164, 176), match='123.555.1234'>
    <re.Match object; span=(190, 202), match='800-555-1234'>
    <re.Match object; span=(203, 215), match='900-555-1234'>
    


```python
# match names for Mr
pat_iter(r'Mr\.?\s[A-Za-z]\w*', text_to_search)
```

    <re.Match object; span=(216, 227), match='Mr. Schafer'>
    <re.Match object; span=(228, 236), match='Mr Smith'>
    <re.Match object; span=(260, 265), match='Mr. T'>
    


```python
# match all names using groups ()
pat_iter(r'M(r|s|rs)\.?\s[A-Za-z]\w*', text_to_search)
```

    <re.Match object; span=(216, 227), match='Mr. Schafer'>
    <re.Match object; span=(228, 236), match='Mr Smith'>
    <re.Match object; span=(237, 245), match='Ms Davis'>
    <re.Match object; span=(246, 259), match='Mrs. Robinson'>
    <re.Match object; span=(260, 265), match='Mr. T'>
    


```python
# try matching all these emails
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
pat_iter(r'[a-zA-Z]+@[a-z]+\.com', emails)
```

    <re.Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>
    


```python
pat_iter(r'[a-zA-Z.0-9-]+@[a-z-]+\.(com|edu|net)', emails)
```

    <re.Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>
    <re.Match object; span=(25, 53), match='corey.schafer@university.edu'>
    <re.Match object; span=(54, 83), match='corey-321-schafer@my-work.net'>
    


```python
# try matching all these urls
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pat_iter(r'https?://[a-z.]+\.(com|gov)', urls)
```

    <re.Match object; span=(1, 23), match='https://www.google.com'>
    <re.Match object; span=(24, 42), match='http://coreyms.com'>
    <re.Match object; span=(43, 62), match='https://youtube.com'>
    <re.Match object; span=(63, 83), match='https://www.nasa.gov'>
    


```python
# using groups to capture information, sub()
# grab only top level domain name (google.com, youtube.com, nasa.gov)
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# here \2\3 are groups 2 which is domain name and group 3 which is top level deomain name
print(pattern.sub(r'\2\3', urls))
```

    
    google.com
    coreyms.com
    youtube.com
    nasa.gov
    
    


```python
# findall returns a list of all matched patterns
pattern = re.compile(r'Mr\.?\s[A-Za-z]\w*')
pattern.findall(text_to_search)
```




    ['Mr. Schafer', 'Mr Smith', 'Mr. T']




```python
# to search within a string, returns only first pattern match
pattern = re.compile(r'sentence')
pattern.search(sentence)
```




    <re.Match object; span=(8, 16), match='sentence'>




```python
# to search for a pattern, ignoring case sensitivity
pattern = re.compile(r'sentence', re.IGNORECASE)
pattern.findall(sentence)
```




    ['sentence', 'seNtEnce', 'sEnteNce', 'SentenCe']




```python
pat_iter(r'\w+', sentence)
```

    <re.Match object; span=(0, 5), match='Start'>
    <re.Match object; span=(6, 7), match='a'>
    <re.Match object; span=(8, 16), match='sentence'>
    <re.Match object; span=(17, 20), match='and'>
    <re.Match object; span=(21, 25), match='then'>
    <re.Match object; span=(26, 31), match='bring'>
    <re.Match object; span=(32, 34), match='it'>
    <re.Match object; span=(35, 37), match='to'>
    <re.Match object; span=(38, 40), match='an'>
    <re.Match object; span=(41, 44), match='end'>
    <re.Match object; span=(45, 53), match='seNtEnce'>
    <re.Match object; span=(54, 62), match='sEnteNce'>
    <re.Match object; span=(63, 71), match='SentenCe'>
    
