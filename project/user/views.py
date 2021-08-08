from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm 
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 
from .forms import UploadForm
from django.core.files.storage import FileSystemStorage
from .models import upload
from django.http import HttpResponse
from django.views.generic import DetailView

#from .models import user
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.models import load_model
from pickle import load
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt
import argparse
   
#################### index#######################################  
def index(request): 
    return render(request, 'user/index.html', {'title':'index'}) 
   
########### register here #####################################  
def register(request): 
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data.get('username') 
            email = form.cleaned_data.get('email') 
            ######################### mail system ####################################  
            htmly = get_template('user/Email.html') 
            d = { 'username': username } 
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email 
            html_content = htmly.render(d) 
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
            msg.attach_alternative(html_content, "text/html") 
            #msg.send() 
            ##################################################################  
            messages.success(request, f'Your account has been created ! You are now able to log in') 
            return redirect('login') 
    else: 
        form = UserRegisterForm() 
    return render(request, 'user/register.html', {'form': form, 'title':'reqister here'}) 
   
################ login forms###################################################  
def Login(request): 
    if request.method == 'POST': 
   
        # AuthenticationForm_can_also_be_used__ 
   
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            form = login(request, user) 
            messages.success(request, f' wecome {username} !!') 
            return redirect('upload_put') 
        else: 
            messages.info(request, f'account done not exit plz sign in') 
    form = AuthenticationForm() 
    return render(request, 'user/login.html', {'form':form, 'title':'log in'}) 

def upload_put(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('output')
            #return HttpResponse('<h1>Uploaded</h1>')

    else:
        form = UploadForm()

    return render(request, 'user/upload.html', {'form': form })
        #return HttpResponse('<h1>Not Uploaded</h1>')


def extract_features(filename, model):
        #try:
        image = Image.open(filename)
            
        #except:
        #    print("ERROR: Couldn't open image! Make sure the image path and extension is correct")
        imag = image.resize((210,210))

        # Converting image to array because xception can only work on rbg three channels so to create 3 channels for bnW image all this
        # from keras.preprocessing.image import img_to_array, array_to_img
        arr = img_to_array(imag)
        arr = np.repeat(arr, 3, -1)
        imag =array_to_img(arr)

        imag = np.array(imag) # This was there before my addition
        # for images that has 4 channels, we convert them into 3 channels
        if imag.shape[2] == 4: 
            imag = imag[..., :3]
        imag = np.expand_dims(imag, axis=0)
        imag = imag/127.5
        imag = imag - 1.0
        feature = model.predict(imag)
        return feature
    
def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def generate_desc(model, tokenizer, photo, max_length):
    in_text = 'start'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        pred = model.predict([photo,sequence], verbose=0)
        pred = np.argmax(pred)
        word = word_for_id(pred, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'end':
            break
    return in_text

tokenizer = load(open("tokenizer.p","rb")) 
model = load_model('model_24.h5')   #Idhar tera pura path de jidhar tune model ko save kiya hai
xception_model = Xception(include_top=False, pooling="avg")
img_path = r'C:\Users\vidhi\Documents\django_app\project\media\images\1003_IM-0005-2002.dcm.png'
max_length = 32

def output(request): 
    if request.method == 'GET': 
         
        images = upload.objects.all() 
        photo = extract_features(img_path, xception_model)
        img = Image.open(img_path)
        description = generate_desc(model, tokenizer, photo, max_length)
        #context = { 'description' : 'images'}
        return render(request, 'user/output.html', {'output': images, 'description': description} )
    #return HttpResponse('successfully uploaded')
'''class output(DetailView):
    model = upload
    template_name = 'user/output.html'
    Context_object_name = 'image'''
