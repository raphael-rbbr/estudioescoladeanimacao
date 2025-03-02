FROM python:3.9.20

RUN mkdir /estudioescoladeanimacao

WORKDIR /estudioescoladeanimacao

ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy the Django project  and install dependencies
COPY requirements.txt  /estudioescoladeanimacao/

# run this command to install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project to the container
COPY . /estudioescoladeanimacao/


# Expose the Django port
EXPOSE 80

# Run Django’s development server
RUN python manage.py collectstatic

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
