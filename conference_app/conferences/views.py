from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Conference, Like


# Create your views here.



# 	Sukurkite ListView, kuris atvaizduotų visas konferencijas
class ConferenceListView(ListView):
    model = Conference
    # Alternatyva ListView klasei:
    # def conference_list( request ):
    #     conferences = Conference.objects.all()
    #     return render( request, "conferences/conference_list.html", { "object_list": conferences })

class ConferenceDetailView (DetailView):
    model = Conference
    # Alternatyva DetailView
    # def conference_detail( request, pk ): # pk ateina iš urls failo: path( "<int:pk>/", ... )
    #     conference = get_object_or_404( Conference, pk = pk )
    #     return render( request, "conferences/conference_detail.html", { "object": conference } )
class ConfeneceLikeView(View):
    def get(self, request, conferencijos_id):
        if not request.user.is_authenticated:
            return redirect('login')
        conference = get_object_or_404(Conference, id=conferencijos_id)
        laiku_kiekis = Like.objects.filter(conference=conference, user=request.user).count()
        if laiku_kiekis > 0:
            return HttpResponse("Jus jau prisiregistravote")

        # event.visitors += 1  # pridedam viena visitor
        # event.save()  # issaugo informacija
        registration = Like()
        registration.event = conference
        registration.user = request.user
        registration.save()
        redirect('conference-detail', conferencijos_id)
