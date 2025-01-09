# Docker File

FROM python:3.9-slim

# Set the working Directory

WORKDIR /CRP_App

# cpoy the applications files

COPY RF_model.pkl /CRP_App/
COPY app.py /CRP_App/
COPY requirements.txt /CRP_App/
COPY templates /CRP_App/templates

# Install dependencies

RUN pip install --no-cache-dir -r requirements.txt


# Expose the flask Port

EXPOSE 5000

# Run the Application

CMD ["python", "app.py"]
