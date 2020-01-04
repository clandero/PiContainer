FROM python:3.7-alpine
COPY src/ /picalc-mpmath
WORKDIR /picalc-mpmath
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python","main.py"]
