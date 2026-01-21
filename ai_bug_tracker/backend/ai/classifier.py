# AI classification code placeholder
def classify_bug(description: str) -> str:
    """
    Very basic rule-based classification.
    Later we can replace with AI model.
    """
    desc = description.lower()
    if "crash" in desc or "data loss" in desc or "not working" in desc:
        return "Critical"
    elif "slow" in desc or "performance" in desc:
        return "Major"
    else:
        return "Minor"
