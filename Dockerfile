FROM python:3.12-slim
WORKDIR /project
ENV PYTHONDONTWRITEBYTECODE=1
COPY . .
CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
