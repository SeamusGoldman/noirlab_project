FROM python:3.12-slim

WORKDIR /code
COPY app /code/app
COPY pyproject.tom /code/pyproject.tom
RUN pip install code

CMD ["celestial-app"]
