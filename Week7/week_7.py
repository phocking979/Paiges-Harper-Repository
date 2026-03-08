def encode_rle(input_string):
    '''
    Converts a string to RLE form,single characters have no count.
    Uses # to escape digits and ## for literal #.

    Args: input_string (str)

    return: encoded_string (str)
    '''
    # Parameter validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    if input_string == "":
        return ""

    encoded = ""
    i = 0

    while i < len(input_string):
        char = input_string[i]
        count = 1

        # Count consecutive characters
        while i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
            count += 1
            i += 1

        # Escape handling
        if char.isdigit():
            encoded += "#" + char
        elif char == "#":
            encoded += "##"
        else:
            encoded += char

        # Add count if >1
        if count > 1:
            encoded += str(count)

        i += 1

    return encoded

def decode_rle(input_string):
    '''
    Decodes an RLE string back to its original form.
    Handles ##00 prefix and # escape sequences.

    Args: input_string (str)

    return: decoded_string (str)
    '''
    # Parameter validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    if input_string == "":
        return ""

    data = input_string

    # Remove encoded marker
    if data.startswith("##00"):
        data = data[4:]

    decoded = ""
    i = 0

    while i < len(data):

        # Handle escape sequences
        if data[i] == "#":

            if i + 1 >= len(data):
                return "Error: Invalid escape sequence"

            if data[i + 1] == "#":
                char = "#"
                i += 2

            elif data[i + 1].isdigit():
                char = data[i + 1]
                i += 2

            else:
                return "Error: Invalid escape sequence"

        else:
            char = data[i]
            i += 1

        # Read count
        count_str = ""

        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1

        if count_str:
            count = int(count_str)

            if count <= 0:
                return "Error: Invalid count in encoded string"
        else:
            count = 1

        decoded += char * count

    return decoded

def main():
    user_input = input("Enter string to process: ")
    
    if not user_input:
        print("Empty input")
        return

    if user_input.startswith("##00"):
        print("Detected encoded format. Decoding:")
        result = decode_rle(user_input)
    else:
        print("Detected raw text. Encoding:")
        result = "##00" + encode_rle(user_input)
        
    print(f"Result: {result}")

if __name__ == "__main__":
    main()