from google import genai

client = genai.Client(api_key="SUA_API_KEY")

while True:
    pergunta = input("Você: ")

    response = client.models.generate_content(
    config ={"system_instruction":"You are a assistent AI, you translate portuguese texts in english texts"},
        model="gemini-2.5-flash",
        contents=pergunta
    )

    print("IA:", response.text)
