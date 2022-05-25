FROM python:3.8

WORKDIR /usr/src/server
ADD requirements.txt .
RUN pip install -r requirements.txt

# uvicornのオプションに--reloadを付与し、
# main.pyの編集と同時に変更内容を反映させる。
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]