from django.shortcuts import render
from django.views.generic import ListView
from . import services
from .models import Pokemon
from .services import get_detail_pokemon, fill_db
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required



def pokemon_list(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, "sitetemplates/index.html", {"users":users})


START = 40
NUMBER = 40

@login_required
def user_profile(request):
    global START
    global NUMBER


    if request.method == 'POST':


        if request.POST.get("more"):

            START = NUMBER + 1
            NUMBER = NUMBER + 10
            fill_db(START, NUMBER)
            messages.success(request, f"✔️ 10 Покемонов  было успешно обнаружено!")
            return HttpResponseRedirect(request.path_info)
        elif request.POST.get("catch"):
            pok = Pokemon.objects.get(id=int(request.POST.get("pokeid")))
            pok.save()
            pok.user.add(request.user)
            messages.success(request, f"✔️ Покемон {pok.name} был успешно добавлен у вашу комманду!")
            return HttpResponseRedirect(request.path_info)
        elif request.POST.get("release"):
            pok = Pokemon.objects.get(id=int(request.POST.get("pokeid")))
            pok.save()
            pok.user.remove(request.user)
            messages.success(request, f"✔️ Покемон {pok.name} был успешно освобождён!")
            return HttpResponseRedirect(request.path_info)


    if Pokemon.objects.filter(id=1).exists() == False:
        fill_db(1, NUMBER)

    pokemons = Pokemon.objects.all()
    return render(request, "sitetemplates/profile.html", {"pokemons":pokemons})