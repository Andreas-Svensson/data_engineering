FROM python:3.11

# host container
ADD main.py .

RUN pip install plotly_express dash

# listen to port
EXPOSE 8050

CMD ["python", "./main.py"]

# then build image file using:
# docker build -t lec1-image .
# -t is tag aka the image name, followed by the image name

# then run image file to create docker container:
# docker run --name lec1_container lec1-image
# name of container followed by name of image to run from

# remove all containers in folder
# docker container prune
# remove specific container
# docker rm <name> i.e. docker rm lec1-container

# run docker:
# docker run -it lec1-image /bin/bash
# gives error from git bash
# go to ubuntu app (already has docker installed) and run the command there
# now inside docker container

# ---

# create venv in repo folder
# python -m venv venv

# activate venv
# source venv/Scripts/activate

# install using pip will install to active environment, in this case venv

