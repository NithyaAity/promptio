FROM python:3.12-slim

WORKDIR /usr/src/app
COPY . .
RUN poetry add gradio
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "main.py"]