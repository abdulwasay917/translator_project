from django.http import JsonResponse
from django.shortcuts import render
from deep_translator import GoogleTranslator


def home(request):
    return render(request, "translator/home.html")


def translate_text(request):
    if request.method == "POST":
        text = request.POST.get("text")
        direction = request.POST.get("direction")

        try:
            if direction == "en_ur":
                translated = GoogleTranslator(source='en', target='ur').translate(text)
            else:
                translated = GoogleTranslator(source='ur', target='en').translate(text)

            return JsonResponse({"translated": translated})

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Invalid request"})