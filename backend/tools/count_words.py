def count_words(text: str):
    """
    Count the number of words in a given text.
    """
    words = text.split()
    return {
        "word_count": len(words)
    }


TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "count_words",
        "description": "Counts the number of words in a given text",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "Text to count words from"
                }
            },
            "required": ["text"]
        }
    }
}
