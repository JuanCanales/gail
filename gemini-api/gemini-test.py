from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.

client = genai.Client(api_key="AIzaSyAtRcCnT4gsBcqubmffKKHajNsWuhMALEw")


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