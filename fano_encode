def fano_encoding(letters):
    if len(letters) == 1:
        return {letters[0]: "0"}
    elif len(letters) == 2:
        return {letters[0]: "0", letters[1]: "1"}
    else:
        freq = {}
        for letter in letters:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        split_index = len(sorted_freq) // 2
        left_group = [x[0] for x in sorted_freq[:split_index]]
        right_group = [x[0] for x in sorted_freq[split_index:]]

        left_codes = fano_encoding(left_group)
        right_codes = fano_encoding(right_group)

        result = {}
        for letter in left_codes:
            result[letter] = "0" + left_codes[letter]
        for letter in right_codes:
            result[letter] = "1" + right_codes[letter]

        return result


sequence = input()
codes = fano_encoding(sequence)

for letter in codes:
    print(letter + " - " + codes[letter])
