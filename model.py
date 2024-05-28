import transformers
import torch

from transformers import AutoTokenizer
import json


class Model:

    pipeline = None

    def __init__(self):
        self.load()

    def get_llama3_model_list(self):
        return;

    def load(self):
        # model_id = "MLP-KTLim/llama-3-Korean-Bllossom-8B"
        # model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
        model_id = "maywell/Llama-3-Ko-8B-Instruct"
        # model_id = "saltlux/Ko-Llama3-Luxia-8B"
        
        tokenizer = AutoTokenizer.from_pretrained(model_id)

        self.pipeline = transformers.pipeline(
            "text-generation",
            tokenizer=tokenizer,
            model=model_id,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device="mps",
        )



    def chat(self, messages):
        prompt = self.pipeline.tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=True
        )

        terminators = [
            self.pipeline.tokenizer.eos_token_id,
            self.pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = self.pipeline(
            prompt,
            max_new_tokens=256,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )
        
        return outputs[0]["generated_text"][len(prompt):]