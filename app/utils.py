def clean_generated_text(text: str) -> str:
    """
    Clean and post-process the generated text.

    Args:
        text (str): The raw generated text.

    Returns:
        str: The cleaned text.
    """
    # Remove any leading/trailing whitespace
    text = text.strip()

    # Optionally, you can add more cleaning logic here, such as:
    # - Removing unwanted tokens
    # - Fixing punctuation
    # - Limiting length

    return text
