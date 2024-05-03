

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

genai.configure(api_key="buraya gemini api key koyacaksınız")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

def generate_sentence(sentence):
  response = model.generate_content(f"{sentence}cümlesinin sonuna hangi kelime gelebilir")
  print(response.text)
  return response.text#cümlenin sonu tahmini


generate_sentence("mustafa kemal paşa")
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