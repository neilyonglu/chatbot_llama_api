from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Message
from .llama_api import llama_api


def chat_view(request):
    Message.objects.all().delete()
    return render(request, 'chat.html')

def reply_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        api_output = llama_api(user_input)
        Message.objects.create(text=api_output)  # 保存消息到數據庫
        return JsonResponse({'message': api_output})