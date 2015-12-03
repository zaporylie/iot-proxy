FROM hypriot/rpi-python
MAINTAINER zaporylie

WORKDIR /var/www/html
VOLUME /var/www/html

ADD ./ /var/www/html

RUN pip install flask pyyaml
RUN cp default.settings.yaml settings.yaml

EXPOSE 80

CMD [ "python", "proxy.yaml" ]
