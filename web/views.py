from django.shortcuts import render, redirect
from .models import *
from .forms import FormContact
from django.contrib import messages
from discord_webhook import DiscordWebhook, DiscordEmbed
from django.conf import settings
# Create your views here.
def index(request):
    proyectos = Project.objects.all()
    context = {
        "proyectos": proyectos
    }
    return render(request, 'pages/index.html', context)

def contact(request):
    if request.method == 'POST':
        formulario = FormContact(request.POST)
        if formulario.is_valid():
            datos_form = formulario.cleaned_data

            email = datos_form.get('email')
            nombre = datos_form.get('nombre')
            asunto = datos_form.get('asunto')
            mensaje = datos_form.get('mensaje')

            webhook = DiscordWebhook(url=settings.WEBHOOK_DC, content='Hay va, parece que vas a tener un nuevo cliente 😊')
            embed = DiscordEmbed(title='Mensaje de contacto', description=f'{nombre} te acaba de contactar', color='03b2f8')
            embed.set_footer(text='System by Jose Manuel')
            embed.set_timestamp()
            embed.add_embed_field(name='Correo electrónico', value=email)
            embed.add_embed_field(name='Nombre', value=nombre)
            embed.add_embed_field(name='Asunto', value=asunto)
            embed.add_embed_field(name='Mensaje', value=mensaje)            
            webhook.add_embed(embed)
            response = webhook.execute()
            messages.success(request, f'Acabas de contactar conmigo, en breves te respondoré', extra_tags='succes_beta')

            return redirect('/')
    else:
        formulario = FormContact()
    return render(request, 'pages/contacto.html', {
        'contacto': formulario
    })