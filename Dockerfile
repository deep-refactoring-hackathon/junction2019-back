FROM python:3.8-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
ENV HOST 0.0.0.0
ENTRYPOINT ["python"]
CMD ["app.py"]
