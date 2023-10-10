from chatgpt_function import chatgpt_wrapper


def test_chatgpt_wrapper():
    @chatgpt_wrapper
    def my_function(my_arg: str) -> str:
        '''This is my function.

        Args:
            my_arg (str): This is my argument.

        Returns:
            str: This is my return value.
        '''
        return "Hello World!" + my_arg

    assert my_function.chatgpt_function() == {
        "name": "my_function",
        "description": "This is my function.",
        "parameters": {
            "type": "object",
            "properties": {
                "my_arg": {
                    "type": "string",
                    "description": "This is my argument."
                }
            },
            "required": [
                "my_arg"
            ]
        },
        "returns": [
            {
                "description": "This is my return value.",
                "type": "string"
            }
        ]
    }

    assert my_function("!") == 'Hello World!!'


def test_chatgpt_wrapper_no_docstring():
    try:
        @chatgpt_wrapper
        def my_function(my_arg: str) -> str:
            return "Hello World!" + my_arg

        my_function.chatgpt_function()
        assert False
    except Exception as e:
        assert isinstance(e, ValueError)


if __name__ == "__main__":
    test_chatgpt_wrapper()
    test_chatgpt_wrapper_no_docstring()
    print("All tests passed!")
