# django-serve-static-file-from-aws-s3
How to config setting to serve user upload files & static files with aws s3 bucket


## Install Packages

* django-storages
* boto3 
* pillow 


## setup .ebextension for Elastic Beanstalk

> [!Note] 
> create  django.config file and add the following code

```
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath:  mypj.wsgi:application
```


# Key Points

## Access File Url in django template file
File object has url & path property  
EX:  src={{car.image.url}}

## How to run development server without applying static(css file) 
`python manage.py runserver --nostatic`

## config DEBUG with environment variable

### config DEBUG in settings.py
`DEBUG = os.getenv('DEBUG') == 'True'`

## serve static file on the same web server

### url.py in root project

```
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('car/', include('car.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \  
+ static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)  
```

# settings.py


> [!NOTE]
> STATIC_URL: The URL of which the static files in STATIC_ROOT directory are served(by Apache or nginx..etc)

`
STATIC_URL = 'static/'  
`

> [!Note]
> STATICFILES_DIRS:  a list of directories where Django will  look for static files.

```
STATICFILES_DIRS=[  
  BASE_DIR / 'static'  
]  
```

> [!Note]
> STATIC_ROOT: The absolute path to the directory where ./manage.py collectstatic will collect static files for deployment.

`
STATIC_ROOT= BASE_DIR / 'staticfiles'  
`

> [!Note]
> MEDIA_URL: URL that handles the media served from MEDIA_ROOT, used for managing stored files.

`
MEDIA_URL="media/"  
`

> [!Note]
> MEDIA_ROOT: The Absolute filesystem path to the directory that will hold user-uploaded files

`
MEDIA_ROOT= BASE_DIR / "uploads"  
`

> [!NOTE]
> * setting for django-storage to use s3 bucket 
> * "default" key : for user upload file 
> * "staticfiles" key: for static files 

```
STORAGES={
    "default":{
        "BACKEND":"storages.backends.s3.S3Storage",
        "OPTIONS":{
            'location':'media'
        }
    },
    "staticfiles":{
        "BACKEND":"storages.backends.s3.S3Storage",
        "OPTIONS":{
            'location':'files'
        }
    }
}
```

```
AWS_ACCESS_KEY_ID=os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=os.getenv('AWS_STORAGE_BUCKET_NAME')

```

# Config AWS S3 Bucket 
* edit **bucket policy**
* enable **Static website hosting**
* edit **cross origin resource sharing**
* disable **Block public access**
* 

## AWS S3 bucket policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{your-bucket-name}/*"
        }
    ]
}
```

## AWS S3 bucket cross origin resource sharing

```
[
    {
        "AllowedHeaders": [],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```



