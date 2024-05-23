

'''
import google.generativeai as genai

genai.configure(api_key="AIzaSyCA5f4J4XsvmdMIXbibsXY79iuZ5mAiKko")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')





response = model.generate_content("ali akşam cümlesinin sonuna hangi kelime gelebilir")
print(response.text)

'''
import google.generativeai as genai

genai.configure(api_key="AIzaSyCFvhWAJ8rzMrIJKpb1lll0-jXn5708p3E")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel(
  'gemini-1.5-pro-latest',
  system_instruction=[
    "You are a linguist and your sole purpose is to correct typos and spelling mistakes in the texts sent to you.",
    "You need to return the new text between two asterisks (**text**)",
    "You can also add to the text yourself if the meaning of the text needs to be improved"
  ]
)

def generate_sentencefonk(sentence):
  response = model.generate_content(f"{sentence}")
  print(response.text)
  return response.text#cümlenin sonu tahmini

generate_sentencefonk("aliye geldi")

'''
çıktısı:
models/gemini-1.0-pro
models/gemini-1.0-pro-001
models/gemini-1.0-pro-latest
models/gemini-1.0-pro-vision-latest
models/gemini-1.5-pro-latest
models/gemini-pro
models/gemini-pro-vision
* Atatürk
* Gazi
* Paşa
* Önder
* Kurtarıcı
* Büyük
'''