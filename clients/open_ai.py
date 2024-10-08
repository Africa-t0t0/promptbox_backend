import openai

class OpenAIClient(object):
    _secret_key = None
    _model = None
    _openai_obj = None
    _minimum_prompt_len = 20

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

    def _set_gpt_4_o_mini(self):
        self._model = "gpt-4o-mini"

    def _get_gpt_model(self) -> str:
        if self._model is None:
            self._set_gpt_3_5_model()
        model = self._model
        return model

    @staticmethod
    def _prepare_message(prompt: str) -> dict:
        dd = {
            "role": "user",
            "content": prompt
        }
        return dd

    def _get_basic_specs(self) -> (str, openai):
        model = self._get_gpt_model()
        openai_obj = self._get_openai_obj()
        return model, openai_obj

    def test_prompt(self) -> None:
        model = self._get_gpt_model()
        openai_obj = self._get_openai_obj()
        response = openai_obj.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": "Haz una historia sobre un perro que lucha contra marcianos."}
            ]
        )

        print(response.choices[0].message["content"])

    def custom_prompt(self, prompt: str) -> str:
        if prompt is None or prompt == "" :
            raise Exception("cannot request with empty prompt.")
        elif len(prompt < self._minimum_prompt_len):
            raise Exception(f"prompt length cannot be less than {self._minimum_prompt_len}.")

        model, openai_obj = self._get_basic_specs()

        message_dd = self._prepare_message(prompt=prompt)
        final_dd = {
            "model": model,
            "content": [message_dd]
        }
        response = openai_obj.ChatCompletion.create(**final_dd)
        response_from_gpt = response.choices[0].message["content"]
        return response_from_gpt

