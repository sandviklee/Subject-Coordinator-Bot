def handleResponses(message) -> str:
    message = message.lower()

    if message == "-help":
        return "Future help..."

    elif message == "-commands":
        return "Commands..."