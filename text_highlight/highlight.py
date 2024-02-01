import regex

def highlight(input_text: str, pattern:str)->str: 
    """ 
    highlight dose to insert () between finding pattern in given string

    :param input_text: given string
    :param pattern: given pattern
    :return string with () between find pattern in given string

    """
    
    result = input_text
    
    match_position = regex.search(pattern, input_text)
   
    if (match_position is not None) and (pattern != ""):
        start_position = match_position.span()[0]
        end_position = match_position.span()[1]

        input_text_list = list(input_text)
        input_text_list.insert(start_position, '(')
        input_text_list.insert(1+end_position, ')')
        result = ''.join(input_text_list)
    return result

if __name__ == '__main__':
    assert(highlight("banana","ana")=="b(ana)na")
    assert(highlight("hello world","ana")=="hello world")
    assert(highlight("hello world","hell")=="(hell)o world")
    assert(highlight("ba","a")=="b(a)")
    assert(highlight("data(sci)","(sci)")=="data((sci))")
    assert(highlight("banana","")=="banana")