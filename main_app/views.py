from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import FeedingForm

# Create your views here.
def home(request): 
	return render(request, 'home.html')

def about(request): 
	return render(request, 'about.html')

def finches_index(request): 
	finches = Finch.objects.all()
	return render(request, 'finches/index.html', {
		'finches': finches 
    }) 

def finches_detail(request, finch_id):
	finch = Finch.objects.get(id=finch_id)
	feeding_form = FeedingForm()
	return render(request, 'finches/detail.html', {
		'finch': finch,
		'feeding_form': feeding_form
	})

class FinchCreate(CreateView):
	model = Finch
	fields = '__all__' #auto generate inputs on the form for all cat inputs
	# fields = ['name', 'breed', 'description', 'age'] - ALTERNATIVE IF WANT TO REORDER THE FIELDS
	# success_url = '/cats' #redirect to the index page

class FinchUpdate(UpdateView):
	model = Finch
	fields = '__all__'

class FinchDelete(DeleteView):
	model = Finch
	success_url = '/finches'

def add_feeding(request, finch_id):
	#create a modelform instance using
	#the data that was submitted in the form
	form = FeedingForm(request.POST)
	if form.is_valid():
		#We want a model instance but we can't
		#save to the DB yet
		#because we haven't assigned the FK (cat id)
		new_feeding = form.save(commit=False)
		new_feeding.finch_id = finch_id
		new_feeding.save()
	return redirect('detail', finch_id=finch_id)