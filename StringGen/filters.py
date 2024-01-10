# filters.py

def incoming(client, message):
    # Implement the logic for incoming messages filter
    if message.text and "keyword" in message.text.lower():  # Modify this condition based on your filter criteria
        return True
    return False  # Message does not meet the criteria

def private(client, message):
    # Implement the logic for private messages filter
    if message.chat.type == "private":
        return True
    return False  # Message is not from a private chat
