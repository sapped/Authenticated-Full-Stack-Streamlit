FROM python:3.9

WORKDIR /streamlit
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY . /streamlit

# Intentionally do not expose port 8501 or else people can circumvent login

RUN pip install pipenv
COPY Pipfile Pipfile.lock /streamlit/
RUN pipenv install --system --dev

RUN pip install "numpy>1.20"
CMD streamlit run app.py