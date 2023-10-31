# django-serve-static-file-from-aws-s3
How to config setting to serve static files using aws s3 bucket

# Access File Url in template file
File object has url & path property  
EX:  src={{car.image.url}}

# How to run development server without applying static(css file) 
python manage.py runserver --nostatic