# String Formatting


```python
person = {'name': 'Jenn', 'age': 23}

# the old way
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

```

    My name is Jenn and I am 23 years old.
    


```python
# a better way
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)
```

    My name is Jenn and I am 23 years old.
    


```python
# much better way
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)
```

    My name is Jenn and I am 23 years old.
    


```python
# much better way can be used like this
tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
```

    <h1>This is a headline</h1>
    


```python
# Accessing class attributes
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

```

    My name is Jack and I am 33 years old.
    


```python
# Keyword arguments
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
print(sentence)
```

    My name is Jenn and I am 30 years old.
    


```python
# better way to access dictionary
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)
```

    My name is Jenn and I am 23 years old.
    


```python
# Padding digits
for i in range(7, 11):
    sentence = 'The value is {:03}'.format(i)
    print(sentence)
```

    The value is 007
    The value is 008
    The value is 009
    The value is 010
    


```python
# formatting decimals
pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)
```

    Pi is equal to 3.14
    


```python
# formatting numbers
sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)
```

    1 MB is equal to 1,000,000 bytes
    


```python
# chaining formatters
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)
```

    1 MB is equal to 1,000,000.00 bytes
    

# Formatting Dates
* [Source](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)


```python
# formatting dates
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)
```

    2016-09-24 12:30:45
    


```python
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)
```

    September 24, 2016
    


```python
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
```

    September 24, 2016 fell on a Saturday and was the 268 day of the year
    

# F-strings (best way)


```python
sentence = f"My name is {person['name']} and I am {person['age']} years old."
print(sentence)
```

    My name is Jenn and I am 23 years old.
    


```python
for i in range(7, 11):
    sentence = f'The value is {i:03}'
    print(sentence)
```

    The value is 007
    The value is 008
    The value is 009
    The value is 010
    


```python
sentence = f'1 MB is equal to {1000**2:,.2f} bytes'
print(sentence)
```

    1 MB is equal to 1,000,000.00 bytes
    
