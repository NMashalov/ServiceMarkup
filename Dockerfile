FROM python:3.11
LABEL description='telegram bot'
COPY pyproject.toml poetry.lock REAMDE.md /opt/app/

RUN poetry install --no-root --only-main --no-interaction && \
    rm -rf ~/.cache/pypoetry

COPY ./chat ./chat 
USER app
CMD ["python","-m","app"]