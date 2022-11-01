# Specifies the version of python to use
FROM python:3.10
# Specifies the port to run the flask app on
EXPOSE 5000
# Navigates to folder within the docker image to store the flask app code
WORKDIR /app
run pip install flask
# Copies content from source to destination
# We could write COPY . /app to copy everything from the current directory
# into the current directory of the image, but since we navigated to /app
# with WORKDIR, we can just say COPY . .
COPY . .
# This specifies which commands to run when the container is spun up
# This allows an external client to the container to make a request to the flask
# app running in the container
CMD ["flask", "run", "--host", "0.0.0.0"]
