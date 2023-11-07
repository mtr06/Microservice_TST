FROM python:3.10.0

WORKDIR /microservice
COPY . .

ADD main.py .

RUN apt-get -y update && apt-get install -y curl gnupg

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# download appropriate package for the OS version
# Debian 11
RUN curl https://packages.microsoft.com/config/debian/11/prod.list  \
    > /etc/apt/sources.list.d/mssql-release.list

RUN exit
RUN apt-get -y update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80", "--reload"]