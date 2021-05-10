FROM python
COPY . /home/ziad/Desktop/docker/project
WORKDIR /home/ziad/Desktop/docker/project
CMD ["python","py.py"]
