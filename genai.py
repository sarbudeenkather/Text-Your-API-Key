from google import genai

client = genai.Client(api_key="YOUR API KEY")

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=["How does AI work?"]
)
print(response.text)
