# django-serve-static-file-from-aws-s3
How to config setting to serve static files using aws s3 bucket

# Main Point

## Access File Url in template file
File object has url & path property  
EX:  src={{car.image.url}}

## How to run development server without applying static(css file) 
python manage.py runserver --nostatic

## serve static file on the same web server

### url.py in root project

from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('car/', include('car.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \  
+ static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)  

### settings.py

STATIC_URL = 'static/'  

STATIC_ROOT= BASE_DIR / 'staticfiles'  

STATICFILES_DIRS=[  
  BASE_DIR / 'static'  
]  

MEDIA_URL="media/"  
MEDIA_ROOT= BASE_DIR / "uploads"  

## setup ebextension

### django.config file

option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath:  mypj.wsgi:application

## config DEBUG with environment variable

DEBUG = os.getenv('DEBUG') == 'True'
