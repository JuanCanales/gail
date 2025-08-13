from google import genai

# API key generada aqui https://aistudio.google.com/u/1/apikey
client = genai.Client(api_key="clave api key")


# Modelo de texto
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Quien es el presidente de españa"
)
print(response.text)


# Modelo de imagen
my_file = client.files.upload(file="./sample2.jpg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[my_file, "Which company belongs"],
)


print(response.text)
