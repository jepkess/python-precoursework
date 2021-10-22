def reverse_sentence(sentence):    
    sentence = sentence.split()

    start_index = 0 #starting index
    end_index = len(sentence)-1 #end index
    while end_index > start_index:
        sentence[start_index], sentence[end_index]=sentence[end_index], sentence[start_index]
        start_index +=1
        end_index -=1
    return f'{" ".join(sentence)}'
    