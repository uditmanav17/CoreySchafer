<a href="https://colab.research.google.com/github/uditmanav17/CoreySchafer/blob/master/Decorators/Decorators.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Decorators - Dynamically Alter The Functionality Of Your Functions
[//]: # "Disclaimer - This is inspired by [this](https://www.youtube.com/watch?v=FsAPt_9Bf3U)."

## Frist class functions and closures
These allows us to treat functions like any other object. We can pass functions as arguments to another function, retuen functions and assign them to variables.

Now, closures allows us to take advantage of first class functions and return the inner function that remembers and has access to local variables of the scope in which they were created.


```python
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function()
```

Notice that the message variable was not created in the inner function, but inner function does have acces to it. Also called free variable.


```python
outer_function()
```

    Hi
    

Okay, simple enough and expected behaviour. Now instead of returning inner_function() lets return inner_function (without paranthesis).


```python
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function

my_func = outer_function()
my_func()  # calling inner function
my_func()  # calling inner function
```

    Hi
    Hi
    

So this is what a closure is. It remembers the message variable even after the outer function has finished executing. Let's modify the outer functiona bit to demonstrate closure.


```python
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

my_func = outer_function('Hello')
my_func()  # calling inner function
my_func2 = outer_function('Bye')
my_func2()  # calling inner function
```

    Hello
    Bye
    

## Decorators
These are function that takes another function as arguments adds some functionality and return another function, all of this without altering the source code of original function. 


```python
# A simple decorator
def deco_fxn(orig_fxn):
    def wrapper_fxn():
        print(f"this is executed by wrapper before exec {orig_fxn.__name__}")
        orig_fxn()
    return wrapper_fxn
```


```python
def display():
    print('Display functon ran')

decorated_display = deco_fxn(display)
decorated_display()

```

    this is executed by wrapper before exec display
    Display functon ran
    

lines 4-5 in above code shell depicts a decorator, but we can also use decorators using @ symbol.
```Python
@deco_fxn
def display():
    print('Display functon ran')
```
This is the same thing as 
```Python 
display = deco_fxn(display)
```
So, lets see an example.


```python
@deco_fxn
def display():
    print('Display functon ran')

display()
```

    this is executed by wrapper before exec display
    Display functon ran
    

So, this decorator wont work if our original function will take any argument. Lets look at an example of a fxn with arguments.
```Python
@deco_fxn
def display_info(name, age):
    print(f"Name - {name} \nage - {age}")

display_info('a', 4)
```
This will cause an error.
```Python
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-27-bbecc8b439d7> in <module>()
      3     print(f"Name - {name} \nage - {age}")
      4 
----> 5 display_info('a', 4)

TypeError: wrapper_fxn() takes 0 positional arguments but 2 were given
```
So, what we need is to be able to pass any number of arguments to our wrapper. We do this by adding *args and **kwargs to our wrapper fxn.


```python
def deco_fxn(orig_fxn):
    def wrapper_fxn(*args, **kwargs):
        print(f"this is executed by wrapper before exec {orig_fxn.__name__}")
        return orig_fxn(*args, **kwargs)
    return wrapper_fxn
```


```python
@deco_fxn
def display_info(name, age):
    print(f"Name - {name} \nage - {age}")
 
display_info('a', 4)
```

    this is executed by wrapper before exec display_info
    Name - a 
    age - 4
    

## Classes as decorators




```python
class deco_class:
    def __init__(self, orig_fxn):
        self.orig_fxn = orig_fxn

    # to mimic the functionality with wrapper we use call
    def __call__(self, *args, **kwargs):
        print(f"this is executed by _call before exec {self.orig_fxn.__name__}")
        return self.orig_fxn(*args, **kwargs)

```


```python
@deco_class
def display_info(name, age):
    print(f"Name - {name} \nage - {age}")
 
display_info('a', 4)
```

    this is executed by _call before exec display_info
    Name - a 
    age - 4
    

## Practical Examples of Decorators


### 1. Logging


```python
# keeps track of how many times a function is exec and with what args
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, kwargs {kwargs}")
        return orig_func(*args, **kwargs)
    
    return wrapper

@my_logger
def display_info(name, age):
    print(f"Name - {name} \nage - {age}")

display_info('Udit', 25)
display_info('Manav', age=25)

```

    Name - Udit 
    age - 25
    Name - Manav 
    age - 25
    

This repetitive functionality is maintained at a single place (decorator) and can easily be used at many places by simply adding decorator to function.
### Timing


```python
def my_timer(orig_func):
    import time
    
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        print(f"{orig_func.__name__} ran in {t2-t1} secs")
        return result

    return wrapper

import time
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f"Name - {name} \nage - {age}")

display_info('Udit', 25)
display_info('Manav', age=25)

```

    Name - Udit 
    age - 25
    display_info ran in 1.0012190341949463 secs
    Name - Manav 
    age - 25
    display_info ran in 1.001225471496582 secs
    

## Chaining decorator
Simply by stacking them one over other.


```python
@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print(f"Name - {name} \nage - {age}")

display_info('Udit', 25)
display_info('Manav', age=25)

```

    Name - Udit 
    age - 25
    wrapper ran in 1.0014264583587646 secs
    Name - Manav 
    age - 25
    wrapper ran in 1.0017378330230713 secs
    

Okay, so it says wrapper ran in x secs. Instead of diaplaying the name of original function we get name of wrapper. What's happening here is that the inner decorator is first executed which returns **wrapper** function. This wrapper(returned by inner decorator) is decorated by the outer decorator which interprets the name of function as wrapper. To rectify this we need to import wraps from functools. Lets try it out, and wrap all of our wrapper with @wraps decorator.


```python
from functools import wraps 

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, kwargs {kwargs}")
        return orig_func(*args, **kwargs)
    
    return wrapper

def my_timer(orig_func):
    import time
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        print(f"{orig_func.__name__} ran in {t2-t1} secs")
        return result

    return wrapper
```


```python
@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print(f"Name - {name} \nage - {age}")

display_info('Udit', 25)
display_info('Manav', age=25)
```

    Name - Udit 
    age - 25
    display_info ran in 1.0014288425445557 secs
    Name - Manav 
    age - 25
    display_info ran in 1.0018949508666992 secs
    

# Decorator with arguments
It is rarely used, you may have encountered when working with Flask framework, but still lets cover it to get an idea how they works. But first a recap.


```python
def decorator_fxn(orig_fxn):
    def wrapper_fxn(*args, **kwargs):
        print(f"executed by wrapper before exec - {orig_fxn.__name__}")
        result = orig_fxn(*args, **kwargs)
        print(f"executed by wrapper after exec - {orig_fxn.__name__}")
        return result
    return wrapper_fxn

@decorator_fxn
def display_info(name, age):
    print(f"display_info called with args - ({name}, {age})")

display_info('Udit', 25)
```

    executed by wrapper before exec - display_info
    display_info called with args - (Udit, 25)
    executed by wrapper after exec - display_info
    

Lets add a prefix to out added functionality. We are gonna do it by adding another layer of function to our decorator and returning the inner function, same as we did previously but with just another layer added.


```python
def prefix_deco(prefix):
    def decorator_fxn(orig_fxn):
        def wrapper_fxn(*args, **kwargs):
            print(f"{prefix}: executed by wrapper before exec - {orig_fxn.__name__}")
            result = orig_fxn(*args, **kwargs)
            print(f"{prefix}: executed by wrapper after exec - {orig_fxn.__name__}")
            return result
        return wrapper_fxn
    return decorator_fxn

@prefix_deco('LOG')
def display_info(name, age):
    print(f"display_info called with args - ({name}, {age})")

display_info('Udit', 25)
```

    LOG: executed by wrapper before exec - display_info
    display_info called with args - (Udit, 25)
    LOG: executed by wrapper after exec - display_info
    
