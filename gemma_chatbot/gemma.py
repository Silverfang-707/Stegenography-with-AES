from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="google/gemma-7b",
  messages=[{"role":"user","content":"what do you think about the name Harshavardan?"}],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

