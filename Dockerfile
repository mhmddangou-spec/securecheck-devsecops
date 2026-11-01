FROM python:3.14-slim

WORKDIR /app

RUN useradd --create-home securecheck

COPY --chown=securecheck:securecheck securecheck.py .
COPY --chown=securecheck:securecheck securecheck_core.py .

USER securecheck

CMD ["python", "securecheck.py"]
