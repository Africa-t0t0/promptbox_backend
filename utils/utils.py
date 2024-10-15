import re


def format_code_blocks(text):
    def format_code(match):
        code = match.group(1)
        formatted_code = f"<pre><code>{code}</code></pre>"
        return formatted_code.replace("\n", "<br>").replace(" ", "&nbsp;")

    formatted_text = re.sub(r"```python(.*?)```", format_code, text, flags=re.DOTALL)
    return formatted_text


def detect_language(text: str) -> str:
    match = re.search(r"```(\w+)", text)
    if match:
        response = match.group(1)
    else:
        response = "unknown"
    return response
