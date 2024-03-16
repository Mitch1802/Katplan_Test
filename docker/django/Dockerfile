ARG PYTHON_VERSION=3.11.2-bullseye

FROM python:${PYTHON_VERSION} as python


FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=production

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
  -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage
ARG BUILD_ENVIRONMENT=production

ARG APP_HOME=/srv/katplan

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN addgroup --system django && \
  adduser --system --ingroup django django && \
  mkdir -p ${APP_HOME}/staticfiles && \
  chown django:django ${APP_HOME}/staticfiles && \
  chmod 775 ${APP_HOME}/staticfiles

RUN mkdir -p ${APP_HOME}/backups && \
  chown django:django ${APP_HOME}/backups && \
  chmod 777 ${APP_HOME}/backups

COPY --chown=django:django ./initial.json ${APP_HOME}/backups/initial.json

RUN apt-get update && apt-get install --no-install-recommends -y \
  libpq-dev \
  gettext netcat \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/

COPY --chown=django:django ./docker/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY --chown=django:django ./docker/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY --chown=django:django ./django ${APP_HOME}

RUN chown django:django ${APP_HOME}

USER django

ENTRYPOINT [ "/entrypoint" ]
