from fastapi import FastAPI
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

app = FastAPI()

model_id = "EleutherAI/pythia-410m"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
  model_id,
  device_map="auto",
)
pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)
@app.get("/")
async def root():
    return {"message": "Welcome to the Language Model API"}


@app.get("/generate/")
async def generate_text(prompt: str , max_new_tokens: int = 50, do_sample:bool = True, temperature:float = 0.7) -> str :
    # Generate text based on the prompt received
    # prompt = f"<s>[INST]{prompt}</INST>"
    response = pipeline(prompt, max_new_tokens=max_new_tokens, do_sample=do_sample, temperature=temperature)

    return response[0]["generated_text"]


@app.post("/generate/batch/")
async def batch_generate_text(prompts: list[str] , max_new_tokens: int = 50, do_sample:bool = True, temperature:float = 0.7) -> list[str] :
    # Generate text based on the prompt received

    prompt = [f"<s>[INST]{p}</INST>" for p in prompts]
    response = pipeline(prompt, max_new_tokens=max_new_tokens, do_sample=do_sample, temperature=temperature)
    print(response)
    return [i[0]["generated_text"] for i in response]