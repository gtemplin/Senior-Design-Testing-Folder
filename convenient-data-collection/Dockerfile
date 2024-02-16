# Based around the python3 image
FROM python:3.10.10

# Set the containers working directory 
WORKDIR /home/admin

# Set the path environment variable 
ENV CURPATH=/home/admin

# Install requirements not in the standard library 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Put local files into the working directory of the image
COPY . .

# Declare the BackupData directory as a volume
#VOLUME /usr/src/app/BackupData
VOLUME /home/admin

# Start running the root process 
CMD ["python", "./RootProcess.py"]

# python 
