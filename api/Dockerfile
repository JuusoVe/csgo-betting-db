FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local directory to the working directory
COPY ./src .

# Run the app.py file
CMD [ "python", "./app.py" ]