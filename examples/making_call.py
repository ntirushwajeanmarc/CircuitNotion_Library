from CircuitNotionAI import CNAI

# Initialize client
client = CNAI.Client(api_key="your_api_key_1")

# Generate content
response = client.models.generate_content(
    model="circuit-2-turbo",
    contents="explain simply how to beat procrastination",
    temperature=0.7,
    max_tokens=200
)
print(response.txt)
