import re
from django.shortcuts import render
from django.http import JsonResponse
from deep_translator import GoogleTranslator


# ---------------------------
# Detect Urdu text
# ---------------------------
def is_urdu(text):
    return any('\u0600' <= c <= '\u06FF' for c in text)


# ---------------------------
# Home
# ---------------------------
def home(request):
    return render(request, "translator/home.html")


# ---------------------------
# Translation API (FINAL STABLE)
# ---------------------------
def translate_text(request):

    if request.method == "POST":

        text = request.POST.get("text", "").strip()
        target = request.POST.get("target", "").strip()

        print("TEXT:", text)
        print("TARGET:", target)

        if not text or not target:
            return JsonResponse({"error": "Missing input"})

        try:
            # STEP 1: detect language
            source = "ur" if is_urdu(text) else "en"

            # STEP 2: prevent same-language bug
            if source == target:
                return JsonResponse({
                    "translated": text,
                    "detected": source
                }, json_dumps_params={'ensure_ascii': False})

            # STEP 3: translate (SAFE MODE)
            translated = GoogleTranslator(
                source="auto",
                target=target
            ).translate(text)

            return JsonResponse({
                "translated": translated,
                "detected": source
            }, json_dumps_params={'ensure_ascii': False})

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Invalid request"})