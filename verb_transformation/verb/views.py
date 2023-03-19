from django.shortcuts import render
from .models import VerbTense
from .forms import VerbTenseForm

def verb_tense_view(request):
    if request.method == 'POST':
        form = VerbTenseForm(request.POST)
        if form.is_valid():
            verb_tense = form.save(commit=False)
            if verb_tense.tense == 'PRESENT':
                verb_tense.make_past()
            verb_tense.save()
    else:
        form = VerbTenseForm()
    
    return render(request, 'index.html', {'form': form})
