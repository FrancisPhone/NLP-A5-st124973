from django.shortcuts import render
from transformers import pipeline, AutoTokenizer
from .models import ChatMessage


tokenizer = AutoTokenizer.from_pretrained("Francis-Phone/gpt2-harmless")
pipe = pipeline("text-generation", model="Francis-Phone/gpt2-harmless", tokenizer=tokenizer)


def chatbot_view(request):

    response_text = ""
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            # Add user message to history
            ChatMessage.objects.create(sender="user", text=prompt)

            # Generate model response
            response_text = pipe(f"\n\nHuman: {prompt}\n\nAssistant:", truncation=True, max_length=128)[0]['generated_text'].split("Assistant:", 1)[1]
            ChatMessage.objects.create(sender="model", text=response_text)

    chat_history = ChatMessage.objects.all().order_by("timestamp")

    return render(request, "chat.html", {"chat_history": chat_history})
