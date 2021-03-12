FROM locustio/locust
RUN pip3 install beautifulsoup4==4.9.3 python-decouple==3.4
#RUN --mount=type=cache,uid=0,target=/app/.cache/pip,from=base pip install -r requirements.txt

