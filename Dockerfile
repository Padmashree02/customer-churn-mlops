FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

#creats docker image (blueprint)-> creates container-> copies requiremnets inside container-> copies entire project-> expose FastAPI port (8000)-> runs FastAPI when container starts