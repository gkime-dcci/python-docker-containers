# current stable python build as of 1/13/25
FROM python:3.12.8

# BASH: get updates and install
RUN apt-get update && apt-get install -y \
# install chromium and chromium driver
    chromium \
    chromium-driver \
# remove package lists after install to reduce package size
    && rm -rf /var/lib/apt/lists/*

# set the workdir to /python-selenium 
WORKDIR /python-selenium

# add main.py contents to the container
COPY main.py .
# copy the contents of requirements to the container
COPY requirements.txt .
# install the packages listed in requirements to the container
RUN pip install -r requirements.txt

# run the command python main.py inside the container
CMD ["python", "main.py"]



