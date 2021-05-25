from transformers import pipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-pt-eo")
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-pt-eo")
tradutor = pipeline("translation_pt_to_eo", model = model, tokenizer = tokenizer)

def traduzir(texto):
    return tradutor(texto, max_length = 40)[0]['translation_text']