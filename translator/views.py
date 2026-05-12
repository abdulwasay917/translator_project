from django.http import JsonResponse
from django.shortcuts import render
from deep_translator import GoogleTranslator
from langdetect import detect


def home(request):
    return render(request, "translator/home.html")


def translate_text(request):
    if request.method == "POST":

        text = request.POST.get("text")
        target = request.POST.get("target")

        try:
            # AUTO detect source language
            detected_lang = detect(text)

            translated = GoogleTranslator(
                source=detected_lang,
                target=target
            ).translate(text)

            return JsonResponse({
                "translated": translated,
                "detected": detected_lang
            })

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Invalid request"})