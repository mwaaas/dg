from mwaaas/dg:0.0.1

ADD . .

RUN chmod u+x run_server.sh

EXPOSE 8000