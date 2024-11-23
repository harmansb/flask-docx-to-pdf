FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create app directory and set non-root user
RUN useradd -m appuser
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Change ownership and switch to non-root user
RUN chown -R appuser:appuser /app
USER appuser

# Expose Flask default port
EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"]
