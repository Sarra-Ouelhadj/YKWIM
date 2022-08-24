def convertToCamelcase(words):
    '''(list) -> string

    Convert a list of strings to a camelCase string.

    >>> convertToCamelcase(["Hello", "World", "Python", "Programming"])
    helloWorldPythonProgramming
    '''
    s = "".join(word[0].upper() + word[1:].lower() for word in words)
    return s[0].lower() + s[1:]

def convertToPascalcase(words):
    '''(list) -> string

    Convert a list of strings to a PascalCase string.

    >>> convertToPascalcase(["Hello", "World", "Python", "Programming"])
    HelloWorldPythonProgramming
    '''
    return "".join(word[0].upper() + word[1:].lower() for word in words) 