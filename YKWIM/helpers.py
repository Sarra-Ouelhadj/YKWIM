from re import sub

def convertToSnakecase(s):
    '''
    >>> ConvertToSnakecase("Hello World Python Programming")
    hello_world_python_programming 
    '''
    return '_'.join(sub('([A-Z][a-z]+)', r' \1',sub('([A-Z]+)', r' \1',s.replace('-', ' '))).split()).lower()

def convertToCamelcase(s):
    '''
    >>> ConvertToCamelcase("Hello World Python Programming")
    helloWorldPythonProgramming 
    '''
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])

def convertToPascalcase(s):
    '''
    >>> convertToPascalcase("Hello World Python Programming")
    HelloWorldPythonProgramming
    '''
    return "".join(w[0].upper() + w[1:].lower() for w in s.split()) 