FROM python:3.11

# copy exercise files to respective directory
COPY logs E1/logs
COPY packages E1/packages
COPY src E1/src

# pip installations
RUN pip install matplotlib plotly_express pandas numpy dash scikit-learn

# no idea what this does
RUN apt-get update

# install nano
RUN apt-get -y install nano

# install cron
RUN apt-get -y install cron

# start cron service
CMD ["cron", "-f"]

# cron schedule script to run every minute and output to log file
RUN echo "* * * * * root /bin/bash -c 'echo -e \"\$(python /E1/logs/countdown.py)\\n\\n\$(cat /E1/logs/countdown.log)\" > /E1/logs/countdown.log'\n" >> /etc/crontab

# set workdir to root/E1
WORKDIR /E1

EXPOSE 8050

CMD ["python", "./src/ex1_0_setup.py"]
