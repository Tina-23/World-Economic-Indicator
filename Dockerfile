FROM python:3.10-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

COPY pyproject.toml .
COPY poetry.lock .

# Install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copy app and model
COPY app ./app
COPY models ./models

EXPOSE 8000
CMD ["gunicorn", "app.main:app", "-b", "0.0.0.0:8000"]
