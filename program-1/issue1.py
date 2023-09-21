def frequency_sort(s):
    # Count the frequency of each character
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    
    # Sort the string based on the character frequency
    sorted_str = ""
    for c, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        sorted_str += c * count
    
    return sorted_str