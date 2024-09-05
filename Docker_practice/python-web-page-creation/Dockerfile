#use official python image as base
FROM python:3.9-slim
#Set the working directory in Container
WORKDIR /app
#Copy the current directory contents into the container at /app
COPY . /app
# Install any dependencies specified in requirement.txt
RUN pip install --no-cache-dir -r requirements.txt
#Make port 80 available to the world outside
EXPOSE 80
#Define environment variable
ENV NAME=World
#Run app.py when container launches
CMD ["python","app.py"]
