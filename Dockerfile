# layer 1
#Base image: NVIDIA CUDA with PyTorch -> FROM 커맨드로 Base image를 가져옴.
#FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-runtime
FROM python:3.10-slim

# layer 2
#Set working directory
WORKDIR /app

# layer 3
#Copy project files - 현재  디렉토리(.) 내의 Dockerfile에서 작업중인 코드들을 도커의 컨테이너-워킹 디렉토리의 위치(.)-에 복사할 거다!
COPY . .

# layer 4
#Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

#Expose port for FastAPI
EXPOSE 8000

#Command to run FastAPI server
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]