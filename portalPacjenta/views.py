from django.shortcuts import render, redirect
from portalPacjenta.models import Lekarz, Placówka, Konsultacja, Profil, Specialization
from django.views import View
from portalPacjenta.forms import VisitReservationForm, profilForm
from django.db.models import Q
from django.views.generic.edit import UpdateView
# Create your views here.




def indexView(request):
    return render(request, 'base.html')

def homeView(request):
    if request.user.is_authenticated:
        visits = Konsultacja.objects.filter(patient_id=request.user)
        return render(request, 'home.html', {'visits':visits})
    else:
        return redirect('/')

def docListView(request):
    specializations = Specialization.objects.all()
    search_term = request.GET.get('search_term')
    if search_term:
        doctors = Lekarz.objects.filter(Q(name__icontains=search_term)| Q(surname__icontains=search_term))
    else:
        doctors = Lekarz.objects.all()
    return render(request, 'doctors.html', {'doctors':doctors, 'specs':specializations})


def placesView(request):
    search_term = request.GET.get('search_term')
    if search_term:
        places = Placówka.objects.filter(Q(city__icontains=search_term) | Q(region__icontains=search_term) | Q(address__icontains=search_term))
    else:
        places = Placówka.objects.all()
    return render(request, 'places.html', {'places': places})


def visitsView(request):
    visits = Konsultacja.objects.filter(patient_id=request.user).order_by("date")
    return render(request, 'visits.html', {'visits': visits})

def placeVisitView(request):
    places = Placówka.objects.all()
    return render(request, 'placesVisit.html', {'places': places})

def doctorVisitView(request, id):
    place = Placówka.objects.get(pk=id)
    doctors = place.doc.all()
    return render(request, 'doctorVisit.html', {'doctors':doctors})

class newVisitForm(View):

    def get(self, request):
        visitReservation = VisitReservationForm()
        return render(request, "reservation.html", {'form': visitReservation})
    def post(self, request):
        form = VisitReservationForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.patient = request.user
            visit.save()
            return redirect('/visits/')
        return render(request, "reservation.html", {'form': form})

def delete_visit(request, pk):
    Konsultacja.objects.filter(id=pk).delete()
    return redirect('/visits/')

class profilFormView(View):

    def get(self, request):
        form = profilForm()
        return render(request, 'updateProfil.html', {'form': form})

    def post(self, request):
        form = profilForm(request.POST)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.user = request.user
            profil.save()
            return redirect('/')

class ProfilUpdateView(UpdateView):
    model = Profil
    fields = ['mail', 'phone']
    success_url = '/'
    template_name = 'profilUpdate.html'


def profilView(request):
    profil = request.user.profil
    return render(request, 'profil.html', {'profil':profil})


def singlePlaceView(request, id):
    place = Placówka.objects.get(pk=id)
    # doctors = Lekarz.objects.filter(placówka__doc=id)
    return render(request, 'singlePlace.html', {'place':place})


