# current stable python build as of 1/13/25
FROM python:3.13-slim

# BASH: get updates and install
RUN apt-get update && apt-get install -y \
  wget \
  gnupg \
  curl \
  unzip 
# install chromium and chromium driver

RUN sudo apt-install \
  chromium \
  chromium-chromedriver \
  libgconf-2-4 \
  libnss3 \
  libgbm1 \
# remove package lists after install to reduce package size
  # && rm -rf /var/lib/apt/lists/*

# Set envronment variables for Chromium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
ENV PYTHONBUFFERED=1

ENV CHROME_OPTIONS="--headless --no-sandbox --disable-dev-shm-usage --disable-gpu"

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



