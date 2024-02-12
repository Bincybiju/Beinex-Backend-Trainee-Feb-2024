def sort(a):  
    words = a.split('-')
    words_sort = sorted(words)
    sorted_sequence = '-'.join(words_sort)
    return sorted_sequence


sequence = input("Enter words separated with hyphen: ")
sorted_sequence = sort(sequence)
print("Sorted words separated with hyphen:", sorted_sequence)
