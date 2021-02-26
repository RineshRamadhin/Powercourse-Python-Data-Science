FROM jupyter/datascience-notebook:notebook-6.2.0

LABEL description = "Powercourse - Python Data Science - Jupyter Notebook"
LABEL maintainer = "Rinesh Ramadhin"

RUN pip install --upgrade pip
RUN pip install jupyter_contrib_nbextensions
RUN pip install jupyter_nbextensions_configurator
RUN pip install autopep8

USER root

RUN jupyter contrib nbextension install
RUN jupyter nbextension enable execute_time/ExecuteTime
RUN jupyter nbextension enable code_prettify/autopep8
RUN jupyter nbextension enable spellchecker/main
RUN jupyter nbextension enable skip-traceback/main
RUN jupyter nbextension enable snippets_menu/main
RUN jupyter nbextension enable toggle_all_line_numbers/main
RUN jupyter nbextension enable varInspector/main

USER jovyan

ADD . /src
WORKDIR /src/notebooks/
