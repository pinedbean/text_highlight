import regex

def highlight_v2(input_text: str, pattern: str)->str:
    """ 
    highlight_v2 dose to insert () between finding all sub-pattern in given string

    :param input_text: given string
    :param pattern: given pattern
    :return string with () between all sub-pattern in given string

    """
    
    output_text = input_text
    final_indexes = []
    _temp_index = []
    matchs = regex.finditer(pattern, input_text, overlapped=True)
    for match in matchs:
        if _temp_index == []:
            start_position = match.span()[0]
            end_position = match.span()[1]
            _temp_index.append(start_position)
            _temp_index.append(end_position)
            previous_end_position = end_position
        else:
            start_position = match.span()[0]
            end_position = match.span()[1]
            if (previous_end_position - start_position ==1) and (len(input_text) != end_position):
                _temp_index[1] = end_position 
            elif (previous_end_position - start_position ==1) and (len(input_text) == end_position):
                _temp_index[1] = end_position
                final_indexes.append(_temp_index)
                _temp_index = []
            else:
                final_indexes.append(_temp_index)
                _temp_index = []
                _temp_index.append(start_position)
                _temp_index.append(end_position)
                previous_end_position = end_position
            
    final_indexes.append(_temp_index) 
    output_text_list = list(input_text)
    for i, index in enumerate(final_indexes):
        if (len(index) != 0) and pattern !="" :
            start_index = index[0]
            end_index = index[1]
            output_text_list.insert((i*2)+start_index, '(')
            output_text_list.insert((i*2)+1+end_index, ')')
            output_text = ''.join(output_text_list)

    return output_text

if __name__ == '__main__':
    assert highlight_v2("bana", "ana") == "b(ana)"
    assert highlight_v2("banana", "ana") == "b(anana)"
    assert highlight_v2("banana anana anna", "ana") == "b(anana) (anana) anna"
    assert highlight_v2("banana", "") == "banana"