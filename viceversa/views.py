from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    count_word = len(user_text.split())
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'count':count_word})

def see(request):
    user_text = request.GET['usertext2']
    return render(request, 'see.html', {'usertext':user_text})