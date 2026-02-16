# Project ML - Medical Images 🏥🧠

Machine Interpretation Of Medical Images using Deep Learning

This project is a **Django-based web application** that performs medical image analysis using pre-trained deep learning models.

Users can upload medical images (e.g., X-ray images), and the system processes them using trained neural network models to generate predictions.

---

## 🚀 Features

- User authentication (Register/Login)
- Upload medical images
- Predict using trained deep learning models (.h5)
- Display prediction results
- Email template support
- Django-based web interface

---

## 🧠 Tech Stack

- Python
- Django
- TensorFlow / Keras
- NumPy
- Pillow
- OpenCV
- HTML Templates (Django)

---

## 📁 Project Structure

```

Project-ML-Medical-Images/
│
├── manage.py
├── model_24.h5
├── model_34.h5
├── tokenizer.p
│
├── project/                # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── user/                   # Django app
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/user/
│
├── media/images/           # Uploaded images
│
└── README.md

````

---

# ⚙️ Installation & Setup

## Step 1: Clone the Repository

```bash
git clone https://github.com/Vidhi1999/Project-ML-Medical-Images.git
cd Project-ML-Medical-Images/project
````

---

## Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Apply Migrations

```bash
python manage.py migrate
```

---

## Step 5: Run the Development Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

# 📸 How It Works

1. User registers/logs in.
2. User uploads a medical image.
3. Image is processed.
4. Pre-trained model (`model_24.h5` or `model_34.h5`) loads.
5. Prediction is generated.
6. Result is displayed on output page.

---

# 📦 Model Files

The following files must remain in the project root:

* `model_24.h5`
* `model_34.h5`
* `tokenizer.p`

⚠️ Do NOT delete or move these files, as the prediction system depends on them.

---

# 📂 Media Files

Uploaded images are stored in:

```
media/images/
```

Make sure MEDIA settings in `settings.py` are configured correctly.

---

# 🔒 Default Django Admin (Optional)

To create a superuser:

```bash
python manage.py createsuperuser
```

Then access:

```
http://127.0.0.1:8000/admin
```

---

# 🛠 Troubleshooting

### ❌ Model not loading?

Make sure:

* TensorFlow version matches model version.
* `.h5` files are in correct location.

### ❌ Media files not displaying?

Ensure in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

# 📜 License

This project is developed for academic and educational purposes.

