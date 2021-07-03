FROM python:3.8-slim-buster

RUN mkdir /mlh_portfolio_aws
COPY requirements.txt /mlh_portfolio_aws
WORKDIR /mlh_portfolio_aws
RUN pip3 install -r requirements.txt

COPY . /mlh_portfolio_aws

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]