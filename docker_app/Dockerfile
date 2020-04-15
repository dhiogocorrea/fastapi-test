FROM python:3.7

WORKDIR /app

COPY ./requirements.txt /app

# apt-get and system utilities
RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential g++\
    && rm -rf /var/lib/apt/lists/*


RUN apt-get update && apt-get install -y unixodbc unixodbc-dev unixodbc-bin
RUN apt-get update && apt-get install -y python3-dev

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list | tee /etc/apt/sources.list.d/msprod.list

RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools


RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt


COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5002"]
