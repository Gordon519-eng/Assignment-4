FROM python:3.13.9
LABEL authors="Owen Van Delst"
ADD historial_converter_vand0708.py .
CMD ["python", "./historial_converter_vand0708.py"]