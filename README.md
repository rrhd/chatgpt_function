# ChatGPT Function Wrapper

## Overview

This project provides a Python function wrapper that simplifies the process of converting functions with docstrings into callable functions for ChatGPT. It parses the docstring of a function and creates a description that ChatGPT can use.

## Installation

You can install this package using pip:

```bash
pip install chatgpt-function
```

## Usage

1. Import the `chatgpt_function` module:

   ```python
   from chatgpt_function import chatgpt_wrapper
   ```

2. Define your function with a docstring using the `@chatgpt_wrapper` decorator:

   ```python
   @chatgpt_wrapper
   def my_function(my_arg: str) -> str:
       '''This is my function.

       Args:
           my_arg (str): This is my argument.

       Returns:
           str: This is my return value.
       '''
       return "Hello World!" + my_arg
   ```

3. Access the function's description using `chatgpt_function()`:

   ```python
   function_description = my_function.chatgpt_function()
   ```

   This will provide you with a JSON-like description that you can use as input to ChatGPT.

4. Use the function in ChatGPT:

   ```python
   from openai import ChatCompletion

   response = ChatCompletion.create(
       messages=messages,
       functions=[function_description],
       **kwargs
   )
   ```

## License

This project is licensed under the MIT License.

MIT License

Copyright (c) 2023 Ron Heichman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
