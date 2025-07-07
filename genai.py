from google import genai

client = genai.Client(api_key="AIzaSyAVT9vnsJsFG8M-cC_8a_E8u5v9UQID-ck")

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=["How does AI work?"]
)
print(response.text)