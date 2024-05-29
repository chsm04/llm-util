import transformers
import torch

from transformers import AutoTokenizer
import json
from env.environment import Environment as env


class LLaMa:

    pipeline = None

    def __init__(self):
        self.load()

    def get_llama3_model_list(self):
        return;

    def load(self):
        """
        라마 파이프 라인 생성
        """
        model_id = env.get_llama3_model_id()
        tokenizer = AutoTokenizer.from_pretrained(model_id)

        self.pipeline = transformers.pipeline(
            "text-generation",
            tokenizer=tokenizer,
            model=model_id,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device="cuda:1",
        )

    def get_message_template(self, user_input):
        PROMPT = '''당신은 유용한 AI 어시스턴트입니다. 사용자의 질의에 대해 친절하고 한국어로 정확하게 답변해야 합니다.'''
        messages = [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": user_input},
        ]

        return messages


    def chat(self, messages):
        prompt = self.pipeline.tokenizer.apply_chat_template(
        self.get_message_template(messages), 
        tokenize=False, 
        add_generation_prompt=True
        )

        terminators = [
            self.pipeline.tokenizer.eos_token_id,
            self.pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = self.pipeline(
            prompt,
            max_new_tokens=500,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )
        
        return outputs[0]["generated_text"][len(prompt):]