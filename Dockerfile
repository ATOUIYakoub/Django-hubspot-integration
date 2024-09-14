FROM python:3.12-slim

WORKDIR /crm_analytics

COPY requirements.txt /crm_analytics//

RUN pip install -r requirements.txt

COPY . /crm_analytics//

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
