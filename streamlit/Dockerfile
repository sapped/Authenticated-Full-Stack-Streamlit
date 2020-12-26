FROM python:3.9

WORKDIR /ui
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY . /ui

# Intentionally do not expose port 8501 or else people can circumvent login

RUN pip install pipenv
COPY Pipfile Pipfile.lock /ui/
RUN pipenv install --system --dev

CMD streamlit run app.py