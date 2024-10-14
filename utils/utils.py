import re


def format_code_response(response):
    code_start = response.find("```python")
    code_end = response.find("```", code_start + len("```python"))

    if code_start != -1 and code_end != -1:
        code = response[code_start + len("```python"):code_end].strip()

        formatted_response = (
                response[:code_start] +
                f"<pre><code class='language-python'>{code}</code></pre>" +
                response[code_end + len("```"):]
        )
        return formatted_response
    else:
        return response

