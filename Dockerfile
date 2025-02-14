# Use an official Python runtime image
FROM python:3.10-slim

# Preventing Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Seting the working directory inside the container
WORKDIR /app

# Installing system dependencies (including gettext for msgfmt and build tools)
RUN apt-get update && apt-get install -y \
    build-essential \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies directly 
# Here we install Django, DRF, debug toolbar, whitenoise, and gunicorn.
RUN pip install --upgrade pip && pip install django djangorestframework django-debug-toolbar whitenoise gunicorn python-decouple

# Copying the entire project into the container
COPY . /app/

# Ensure environment variables are available inside the container
ENV SECRET_KEY="insecure-secret-key-for-build"
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=admin123

# Apply database migrations
RUN python manage.py migrate

# Collect static files (using WhiteNoise for static file serving in production)
RUN python manage.py collectstatic --noinput

# Compile translations to support Arabic and other languages
RUN django-admin compilemessages

# Automatically create a superuser if it doesn't exist
RUN echo "from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists() or \
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" \
    | python manage.py shell

# Exposeing the port Gunicorn will run on
EXPOSE 8000

# Starting the application using Gunicorn. 
CMD ["gunicorn", "ai_blog.wsgi:application", "--bind", "0.0.0.0:8000"]
