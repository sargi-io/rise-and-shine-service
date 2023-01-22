FROM continuumio/anaconda3

RUN conda update conda
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml

ENV PATH /opt/conda/envs/myenv/bin:$PATH

COPY . /app
WORKDIR /app

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]