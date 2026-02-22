from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from PIL import Image
from django.http import JsonResponse
from .ml import predict_pil

def home(request):
    return render(request, "home.html")

@require_http_methods(["POST"])
def predict(request):
    uploaded = request.FILES.get("photo")
    if not uploaded:
        return render(request, "home.html", {"error": "No image uploaded."})

    try:
        img = Image.open(uploaded)
    except Exception:
        return render(request, "home.html", {"error": "That file doesn’t look like a valid image."})

    pred = predict_pil(img)
    return render(request, "home.html", {"pred": pred})


@require_http_methods(["POST"])
def predict_api(request):
    uploaded = request.FILES.get("photo")
    if not uploaded:
        return JsonResponse({"error": "No image uploaded."}, status=400)

    try:
        img = Image.open(uploaded)
    except Exception:
        return JsonResponse({"error": "Invalid image file."}, status=400)

    pred = predict_pil(img)
    return JsonResponse(pred)

from django.shortcuts import render

def intro(request):
    return render(request, "intro.html")

def about(request):
    return render(request, "about.html")