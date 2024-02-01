import regex

def find_indexes(input_text: str,pattern:str)-> list:
    """ 
    find_indexes dose to find start indexes of sub pattern from given string

    :param input_text: given string
    :param pattern: given pattern
    :return list of start index of each sub pattern

    """
    result = []
    matchs = regex.finditer(pattern,input_text, overlapped=True)
    if (matchs is not None) and (pattern != ""):
        for match in matchs:
            start_position = match.span()[0]
            result.append(start_position)
    return result
    
if __name__ == '__main__':
    assert find_indexes("banana", "ana") == [1,3]
    assert find_indexes("hello world", "ana") == []
    assert find_indexes("aaaaa","a") == [0,1,2,3,4]
    assert find_indexes("banana","") == []