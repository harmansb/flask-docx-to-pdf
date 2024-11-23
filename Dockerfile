FROM python:3.9-slim


ENV PYTHONUNBUFFERED=1


RUN useradd -m appuser
WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


RUN chown -R appuser:appuser /app
USER appuser


EXPOSE 5000


CMD ["python", "run.py"]
