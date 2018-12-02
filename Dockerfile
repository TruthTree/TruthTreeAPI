FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /truthtree
WORKDIR /truthtree
ADD . /truthtree
COPY .env.production /truthtree/.env
RUN pip install pipenv
RUN pipenv --python 3.7
RUN pipenv install --dev
EXPOSE 8000
CMD ["pipenv", "run" ,"python3", "manage.py", "runserver", "0.0.0.0:8000"]