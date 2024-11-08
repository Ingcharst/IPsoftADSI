import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
# Create your views here.
from django.contrib.auth.decorators import permission_required, login_required
from .models import Medicamento, Receta, Paciente
from .forms import RecetaForm,MedicamentoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm



def inicio(request):
    return render(request, 'inicio.html')



def index(request):
    pacientes_Atendidos = Paciente.objects.filter(estado='Atendido').count() 
    pacientes_Espera = Paciente.objects.filter(estado='Espera').count()
    total_pacientes = Paciente.objects.count()
    Medicamentos_porEntrega = Receta.objects.filter(estado='Falta de medicamento').count()
    context = { 
        'pacientes_Atendidos': pacientes_Atendidos, 
        'pacientes_Espera': pacientes_Espera,
        'total_pacientes': total_pacientes,  
        'Medicamentos_porEntrega': Medicamentos_porEntrega,
          }
    return render(request, 'index.html',context)


def atencion_medica(request):
   pacientes_en_espera = Paciente.objects.filter(estado='Espera') 
   context = { 'pacientes': pacientes_en_espera,}
   return render(request, 'Atención_Medica.html', context)





def historial_clinico(request, paciente_id): 
    paciente = get_object_or_404(Paciente, id=paciente_id) 
    recetas = Receta.objects.filter(paciente=paciente) 
    
    if request.method == 'POST':
        form = RecetaForm(request.POST) 
        if form.is_valid():
            receta = form.save(commit=False) 
            receta.paciente = paciente 
            receta.save()
            paciente.estado = 'Atendido'
            paciente.save() 
            return redirect('index')
    
        else:
            context = { 
                'paciente': paciente, 
                'recetas': recetas, 
                'form': form, 
                } 
            return render(request, 'historial_clinico.html', context)
    form = RecetaForm()
    context = { 
        'paciente': paciente, 
        'recetas': recetas,
            'form': form, } 

    return render(request, 'historial_clinico.html',context)


def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    recetas = Receta.objects.filter(paciente=paciente, estado='Falta de medicamento')
    return render(request, 'detalle_paciente.html', {'paciente': paciente, 'recetas': recetas})


def lista_pacientes_pendientes(request):
    pacientes_pendientes = Paciente.objects.filter(receta__estado='Falta de medicamento').distinct()
    return render(request, 'lista_pacientes_pendientes.html', {'pacientes': pacientes_pendientes})


def detalle_paciente_suministrado(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    recetas = Receta.objects.filter(paciente=paciente, estado='Suministrado')
    return render(request, 'detalle_paciente_suministrado.html', {'paciente': paciente, 'recetas': recetas})

# ///////////////////////////////////////////////////////////

#            Login

# /////////////////////////////////////////////////////////

def iniciar_sesion(request): 
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) 
        if user is not None: 
            login(request, user) 
            return redirect('index') # Redirigir a la página de inicio o a cualquier otra página después del inicio de sesión 
        else: # Manejar el error de autenticación 
          return render(request, 'registration/login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    else: 
     return render(request, 'registration/login.html')

def cerrar_sesion(request): 
    logout(request) 
    return redirect(request,'index.html')


def registro(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): form.save() 
        return redirect('login') 
    else: form = UserCreationForm() 
    return render(request, 'registration/register.html', {'form': form})












# ///////////////////////////////////////////////////////////

#            Modulo de Farmacia 

# /////////////////////////////////////////////////////////

@login_required
@permission_required('Farmacia.can_access_farmacia') 
def lista_medicamentos(request): 
    medicamentos = Medicamento.objects.all() 
    return render(request, 'lista_medicamentos.html', {'medicamentos': medicamentos})

@login_required
@permission_required('Farmacia.can_access_farmacia') 
def lista_recetas(request): 
    recetas = Receta.objects.all() 
    return render(request, 'lista_recetas.html', {'recetas': recetas})


@login_required
@permission_required('Farmacia.can_access_farmacia') 
def entregar_receta(request, receta_id):
    receta = Receta.objects.get(id=receta_id)
    form = RecetaForm(instance=receta)
    if request.method == "POST":
            form = RecetaForm(request.POST,instance=receta)
            if form.is_valid():
                receta.estado = 'Entregado'
                receta.fecha_entrega = timezone.now()
                form.save()
            return lista_recetas_pendientes (request)
    
    return render(request, 'entregar_receta.html', {'form': form, 'receta': receta})
 


@login_required
@permission_required('farmacia.can_access_farmacia') 
def lista_recetas_entregadas(request): 
    recetas_entregadas = Receta.objects.filter(estado='Entregado') 
    return render(request, 'lista_recetas_entregadas.html', {'recetas': recetas_entregadas})               


@login_required
@permission_required('farmacia.can_access_farmacia') 
def lista_recetas_pendientes(request):
    recetas = Receta.objects.filter(estado='Falta de medicamento')
    return render(request, 'lista_recetas_pendientes.html', {'recetas': recetas})


def agregarMedicamentos(request):
  #if request.user.is_authenticated:
    form = MedicamentoForm()
    if request.method == "POST":
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save() 
        return Medicamento(request)
    return render(request, 'Farmacia/agregarmedicamento.html', {"form": form})
    

def actualizarMedicamento(request,id):
 # if request.user.is_authenticated:
    medicamento = Medicamento.objects.get(id=id)
    form = MedicamentoForm(instance=medicamento)
    if request.method == "POST":
        form = MedicamentoForm(request.POST,instance=medicamento)
        if form.is_valid():
            form.save()
        return medicamento(request)
    return render(request, 'Farmacia/agregarmedicamento.html', {"form": form})
    
 # return redirect(index)

def eliminarMedicamento(request,id):
 # if request.user.is_authenticated:
    medicamento = Medicamento.objects.get(id=id)
    medicamento.delete()
    return medicamento(request)
