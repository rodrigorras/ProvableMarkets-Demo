# Build stage
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/install -r requirements.txt

# Runtime stage
FROM python:3.12-alpine

# Install runtime dependencies (for timezone support)
RUN apk add --no-cache tzdata

# Set working directory
WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /install /usr/local/lib/python3.12/site-packages

# Copy the application code
COPY main.py .

# Expose port 8000
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]