from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Artiste,Song,Lyric
# from .serializers import musicSerializer


# def Musics(request):
#     artiste = Artiste.objects.all()
#     musicSerializer(artiste, many= True)
#     return jsonResponse(serializers.data , safe=False)
# # Create your views here.

def Musics(request):
    return render(request, 'index.html')
