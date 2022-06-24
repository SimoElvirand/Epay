from email.message import EmailMessage

from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q
from django.http import HttpResponse, BadHeaderError
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from .form import forgotPasswordForm
from .formModif import FormulaireEntrepriseM
from .models import Entreprise
from .formEntreprise import FormulaireEntreprise
from django.contrib.auth.models import User
from django.contrib import messages
from ProjetSalariApp import settings



# Create your views here.
from .tokens import generate_token


def Valid(request):
    return render(request, 'Entreprise/Validation.html')


def Inscription(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if User.objects.filter(fname=fname):
        # messages.error(request, "Cette entreprise exite déjà, veillez reéssayez avec un autre nom d'entreprise'il vous plaît")
        # return redirect('Inscrit')

        if User.objects.filter(email=email):
            messages.error(request, "Cette Email exite déjà, veillez reéssayez avec un autre Email s'il vous plaît")
            return redirect('inscrit')

        if pass1 != pass2:
            messages.error(request, "Les deux mot de passe doivent être identique!")
            return redirect('inscrit')

        if not fname.isalnum():
            messages.error(request, "Le nom de l'entreprise doit comporter les caractères alpha-Numerique!")
            return redirect('inscrit')

        if not username.isalnum():
            messages.error(request, "Le nom d'utilisateur doit comporter les caractères alpha-Numerique!")
            return redirect('inscrit')

        myuser = User.objects.create_superuser(username, email, pass1)
        myuser.first_name = fname
        myuser.save()

        messages.success(request,
                         "Votre compte a été crée avec succès. Un message de confirmation a été envoyé dans votre boite Email, veillez le confirmer pour activer votre compte")

        # Bienvynue Email

        subject = "Bienvenue dans SalariApp !!"
        message = "Hello" + myuser.first_name + "!! \n" + "Merci pour avoir choisi SalariApp pour la gestion de vos salaire \n Ceci est un message de confirmation, veillez le confirmer pour activer votre compte. \n\n\n Merci \n SalariApp "
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('login')

    return render(request, 'Entreprise/Inscription.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if pass1 != pass2:
            messages.error(request, "Erreur de mot de passe!")
            return redirect('login')

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "Dashbord/Dashbord.html", {'fname': fname})
        else:
            messages.error(request, "Erreur de connexion, veillez entrer les informations correctes")
            return redirect('login')

    return render(request, "Entreprise/Login.html")

@login_required
def AjoutEntrepise(request):
    monformEntreprise = FormulaireEntreprise()
    if request.method == 'POST':
        monformEntreprise = FormulaireEntreprise(request.POST)
        print(1)
        if monformEntreprise.is_valid():
            print(2)
            user = request.user
            nomEntreprise = user.first_name
            #nomEntreprise = monformEntreprise.cleaned_data.get('fname')
            activite = monformEntreprise.cleaned_data.get('activite')
            adresse = monformEntreprise.cleaned_data.get('adresse')
            anneeCreation = monformEntreprise.cleaned_data.get('anneeCreation')
            effectif = monformEntreprise.cleaned_data.get('effectif')
            capital = monformEntreprise.cleaned_data.get('capital')
            chiffreAffaire = monformEntreprise.cleaned_data.get('chiffreAffaire')
            nomDirecteur = monformEntreprise.cleaned_data.get('nomDirecteur')
            numeroContribuable = monformEntreprise.cleaned_data.get('numeroContribuable')
            formeJuridique = monformEntreprise.cleaned_data.get('formeJuridique')

            Entreprisef = Entreprise(nomEntreprise=nomEntreprise, activite=activite, adresse=adresse, anneeCreation=anneeCreation,
                                     effectif=effectif, capital=capital, chiffreAffaire=chiffreAffaire, nomDirecteur=nomDirecteur,
                                     numeroContribuable=numeroContribuable, formeJuridique=formeJuridique)
            print(3)
            Entreprisef.save()
            print(4)
            return redirect('Entre')
        print(5)
    context = {'monformEntreprise': monformEntreprise, }
    return render(request, 'Entreprise/AjoutEntre.html', context)

@login_required
def modifientreprise(request, entreprise_id):
    entreprise= get_object_or_404(Entreprise, id=entreprise_id)
    dic = {'nomEntreprise': entreprise.nomEntreprise,
           'adresse': entreprise.adresse,
           'anneeCreation': entreprise.anneeCreation,
           'activite': entreprise.activite,
           'effectif': entreprise.effectif,
           'capital': entreprise.capital,
           'nomDirecteur': entreprise.nomDirecteur,
           'numeroContribuable': entreprise.numeroContribuable,
           'formeJuridique': entreprise.formeJuridique,
           'chiffreAffaire': entreprise.chiffreAffaire}


    form_em = FormulaireEntrepriseM(data=dic)
    if request.method == 'POST':
        form_em = FormulaireEntrepriseM(request.POST, instance=entreprise)
        if form_em.is_valid():
            form_em.save()
            return redirect('entreprise')
    if request.method =='GET':
        form_em = FormulaireEntrepriseM(data=dic)
    return render(request, 'Entreprise/modifEntreprise.html', {'modifientreprise': form_em})

@login_required
def Entreprisek(request):
    try:
        entreprises = Entreprise.objects.all()
        for element in entreprises:
            print(element.nomEntreprise)
    except:
        a=False
    else:
        a= True
    context={'cle': entreprises}
    return render(request, 'Entreprise/Entreprise.html', context)

@login_required
def Info_Entreprise(request):
    Entreprises = Entreprise.objects.all()
    context = {'Entreprises': Entreprises}
    return render(request, 'Entreprise/InfoEntreprise.html', context)

@login_required
def AfficheNomEntreprise(request):
    entreprise = Entreprise.object.all()
    context = {'entreprise':entreprise}
    return render(request, 'Dashbord/Dashbord.html', context)

#================================================EXTRA=====================================================

                                                           #||


@login_required                                                                                                      #||
def Parametre(request):                                                                                 #||
    return render(request, 'Parametre.html')                                                            #||

@login_required                                                                                                   #||
def Apropos(request):                                                                                   #||
    return render(request, 'Apropos.html')                                                              #||

@login_required                                                                                                       #||
def Contact(request):                                                                                   #||
    return render(request, 'Contact.html')                                                              #||

@login_required                                                                                                        #||
def Aide(request):                                                                                      #||
    return render(request, 'Aide.html')                                                                 #||
                                                                                                        #||
#=========================================================================================================


#=====================================================DECONEXION==========================================
def Finish(request):                                                                                    #||
    logout(request)                                                                                     #||
    return redirect('login')                                                                            #||
#==========================================================================================================

def password_reset_request(request):
    if request.method == "POST":
        print('bonjour post')
        password_reset_form = forgotPasswordForm(request.POST)
        print(password_reset_form)
        if password_reset_form.is_valid():
            print('valid')
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            current_site = get_current_site(request)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Reinitialisation du mot de passe Epay"
                    message = render_to_string('Entreprise/password_reset_email.txt', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': generate_token.make_token(user),
                        'protocol': 'http',
                    })
                    email = EmailMessage(
                        subject, message, settings.EMAIL_HOST_USER, [user.email]
                    )

                    email.fail_silently = True
                    try:
                        email.send()
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset_done")
    password_reset_form = forgotPasswordForm()
    return render(request, 'Entreprise/forgotpass.html', context={"password_reset_form": password_reset_form})
