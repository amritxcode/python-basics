import string

def create_matrix(key):
    key = key.upper().replace("J", "I")
    seen, cleaned_key = set(), []
    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char); cleaned_key.append(char)
    for char in string.ascii_uppercase:
        if char != "J" and char not in seen:
            seen.add(char); cleaned_key.append(char)
    return [cleaned_key[i * 5:(i + 1) * 5] for i in range(5)]

def prepare_text(text):
    text = "".join([c.upper() for c in text if c.isalpha()]).replace("J", "I")
    prepared, i = [], 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i + 1] if (i + 1) < len(text) else "X"
        if char1 == char2: prepared.append(char1 + "X"); i += 1
        else: prepared.append(char1 + char2); i += 2
    return prepared

def process_pairs(pairs, matrix, mode="encrypt"):
    shift = 1 if mode == "encrypt" else -1
    result = []
    for char1, char2 in pairs:
        r1, c1 = next((r, c) for r, row in enumerate(matrix) for c, char in enumerate(row) if char == char1)
        r2, c2 = next((r, c) for r, row in enumerate(matrix) for c, char in enumerate(row) if char == char2)
        if r1 == r2: result.append(matrix[r1][(c1 + shift) % 5]); result.append(matrix[r2][(c2 + shift) % 5])
        elif c1 == c2: result.append(matrix[(r1 + shift) % 5][c1]); result.append(matrix[(r2 + shift) % 5][c2])
        else: result.append(matrix[r1][c2]); result.append(matrix[r2][c1])
    return "".join(result)

if __name__ == "__main__":
    key, message = "CPP", "PYTHON"
    matrix = create_matrix(key)
    pairs = prepare_text(message)
    print(f"Ciphertext: {process_pairs(pairs, matrix)}")
