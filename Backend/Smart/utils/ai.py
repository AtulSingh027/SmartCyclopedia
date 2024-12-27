import google.generativeai as genai
from config import api
# Configure the API key
genai.configure(api_key=api)

# Create model instance
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate response
response = model.generate_content(f"")

# Print response
print(response.text)