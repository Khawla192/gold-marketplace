from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Store, Piece

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def store_index(request):
    stores = Store.objects.all()
    # stores = Store.objects.filter(user=request.user)
    # stores = request.user.store_set.all()
    return render(request, 'stores/index.html', {'stores': stores})

@login_required
def store_detail(request, store_id):
    store = Store.objects.get(id=store_id)
    pieces = store.pieces.all()
    return render(request, 'stores/detail.html', {
        'store': store,
        'pieces': pieces
    })

@login_required
def associate_piece(request, store_id, piece_id):
    Store.objects.get(id=store_id).pieces.add(piece_id)
    return redirect('store-detail', store_id=store_id)

class StoreCreate(LoginRequiredMixin, CreateView):
    model = Store
    fields = ['name', 'description', 'phone_number', 'picture_url', 'links']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class StoreUpdate(LoginRequiredMixin, UpdateView):
    model = Store
    fields = ['description', 'phone_number', 'picture_url', 'links']

class StoreDelete(LoginRequiredMixin, DeleteView):
    model = Store
    success_url = '/stores/'

class PieceCreate(LoginRequiredMixin, CreateView):
    model = Piece
    fields = '__all__'
    
class PieceList(LoginRequiredMixin, ListView):
    model = Piece

class PieceDetail(LoginRequiredMixin, DetailView):
    model = Piece
    template_name = 'main_app/piece_detail.html'

class PieceUpdate(LoginRequiredMixin, UpdateView):
    model = Piece
    fields = ['name', 'grams', 'karat']

class PieceDelete(LoginRequiredMixin, DeleteView):
    model = Piece
    success_url = '/pieces/'

@login_required
def remove_piece(request, store_id, piece_id):
    store = Store.objects.get(id=store_id)
    piece = Piece.objects.get(id=piece_id)
    store.pieces.remove(piece)
    return redirect('store-detail', store_id=store.id)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Create a default store for the new user
            Store.objects.create(
                user=user,
                name=f"{user.username}'s Store",
                description="Default store description",
                phone_number="0000000000",
                picture_url="",
                links=""
            )
            return redirect('store-index')
    else:
        error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
