from django.shortcuts import render, redirect
from .models import ModeloBlog
from .forms import ModeloBlogFormularfio, ModeloBlogForm


def subirblog(request):
    poster=ModeloBlog.objects.all()
    form=ModeloBlogFormularfio()
    if request.method=='POST':
        form=ModeloBlogFormularfio(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Formulario válido. Datos guardados.")
            return redirect('blogs')
        
    return render(request, 'blogs.html', {'poster':poster, 'form':form})

def eliminar(request, m_id):
    poster=ModeloBlog.objects.get(pk=m_id)
    if poster:
        
        poster.delete()
        
    return redirect('blogs')

def editar(request, m_id):
    poster = ModeloBlog.objects.get(pk=m_id)

    if request.method == 'POST':
        form = ModeloBlogForm(request.POST, request.FILES, instance=poster)
        if form.is_valid():
            form.save()
            
            return redirect('blogs')  # Cambia 'blogs' al nombre de la URL a la que deseas redirigir
        
    else:
        form = ModeloBlogForm(instance=poster)

    
    return render(request, 'editar.html', {'form': form, 'poster': poster})
