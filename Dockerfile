FROM python:3.7

RUN apt-get update && apt-get install -y netcat-openbsd && apt-get install -y jq

ARG project_dir=/server

WORKDIR $project_dir

ADD . $project_dir

RUN pip install -r requirements.txt

EXPOSE 5000

#CMD [ "python", "manage.py", "runserver" ]

RUN chmod +x $project_dir/docker-entrypoint.sh

CMD ["/bin/bash", "/server/docker-entrypoint.sh"]