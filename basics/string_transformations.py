"""
Basic string transformations using Python built-in methods.
"""

def transform_text(text):
    upper_text = text.upper()
    lower_text = text.lower()
    swapped_text = text.swapcase()
    
    return upper_text, lower_text, swapped_text


def main():
    text = "Hola mundo"
    
    upper_text, lower_text, swapped_text = transform_text(text)
    
    print(f"Original: {text}")
    print(f"Mayúsculas: {upper_text}")
    print(f"Minúsculas: {lower_text}")
    print(f"Swapcase: {swapped_text}")


if __name__ == "__main__":
    main()
