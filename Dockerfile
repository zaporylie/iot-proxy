FROM hypriot/rpi-python
MAINTAINER zaporylie

WORKDIR /var/www/html
VOLUME /var/www/html
EXPOSE 5000

RUN pip install flask pyyaml requests

ENV PORT=5000
ENV DEBUG=TRUE

ADD ./ /var/www/html

CMD [ "python", "web.py" ]
