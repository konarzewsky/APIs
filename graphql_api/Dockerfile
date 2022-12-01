FROM python:3.10.8-slim

RUN useradd --create-home konarzewsky
USER konarzewsky
ENV PATH="/home/konarzewsky/.local/bin:${PATH}"

WORKDIR /home/konarzewsky

RUN pip install --upgrade pip wheel

COPY --chown=konarzewsky ./requirements.main.txt /tmp/requirements.main.txt
RUN pip install --user -r /tmp/requirements.main.txt

COPY --chown=konarzewsky ./graphql_api/requirements.txt /tmp/requirements.txt
RUN pip install --user -r /tmp/requirements.txt

COPY --chown=konarzewsky . /app

WORKDIR /app

RUN pip install --user -e .
