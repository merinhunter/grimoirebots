FROM python:3.11.0b5-slim

# Python settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Poetry settings
ENV POETRY_VERSION=1.1.14
ENV POETRY_HOME=/etc/poetry
ENV POETRY_VIRTUALENVS_CREATE=false

# Install OS packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH=$POETRY_HOME/bin:$PATH

WORKDIR /code

# Install dependencies
COPY poetry.lock pyproject.toml /code/
RUN poetry install

# Copy Grimoirebots files
COPY . /code/

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "grimoirebots.wsgi"]
