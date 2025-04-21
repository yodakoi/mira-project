from llama_cpp import Llama

# Charger the LLama model or Mistral
llm = Llama(model_path="/app/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf")

def get_ai_response(prompt):
    output = llm("Tu es un assistant Intelligent. {prompt}", max_tokens=100)
    return output['choices'][0]['text']
    