FROM alpine:latest
RUN apk update && apk add bash
pip install -r requirements.txt

WORKDIR /app
COPY split.sh /app`
CMD ["bash", "split.sh"]