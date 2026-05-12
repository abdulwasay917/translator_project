from django.shortcuts import render
from deep_translator import GoogleTranslator

def home(request):
    translated = ""
    text = ""

    if request.method == "POST":
        text = request.POST.get("text")
        direction = request.POST.get("direction")

        if direction == "en_ur":
            translated = GoogleTranslator(source='en', target='ur').translate(text)

        elif direction == "ur_en":
            translated = GoogleTranslator(source='ur', target='en').translate(text)

    return render(request, "translator/home.html", {
        "translated": translated,
        "text": text
    })