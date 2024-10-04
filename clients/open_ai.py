import openai

class OpenAIClient(object):
    _secret_key = None
    _model = None
    _openai_obj = None

    def __init__(self, secret_key: str = None, model: str = None) -> None:
        self._secret_key = secret_key
        self._model = model
        self._openai_obj = self._get_openai_obj()
        self._model = self._get_gpt_model()


    def _set_openai_obj(self):
        self._openai_obj = openai
        self._openai_obj.api_key = self._secret_key


    def _get_openai_obj(self) -> openai:
        if self._openai_obj is None:
            self._set_openai_obj()
        openai_obj = self._openai_obj
        return openai_obj

    def _set_gpt_3_5_model(self):
        self._model = "gpt-3.5-turbo"

    def _get_gpt_model(self) -> str:
        if self._model is None:
            self._set_gpt_3_5_model()
        model = self._model
        return model

    def test_prompt(self) -> None:
        model = self._get_gpt_model()
        openai_obj = self._get_openai_obj()
        response = openai_obj.Completion.create(
            model=model,
            prompt="Escribe una historia corta",
            max_tokens=1
        )

        print(response.choices[0].text)