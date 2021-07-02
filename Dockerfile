FROM python:3.8-slim-buster

RUN mkdir /mlh_portfolio_aws
COPY requirements.txt /mlh_portfolio_aws
WORKDIR /mlh_portfolio_aws
RUN pip3 install -r requirements.txt

COPY . /mlh_portfolio_aws

CMD ["gunicorn", "wsgi:app", "-w 4", "-b 0.0.0.0:80"]
