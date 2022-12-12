# Dockerfile, Image, Container
FROM python:3.9

ADD main.py .
ADD test.py .
ADD eaterlog.csv .
ADD eaterlog1.csv .
ADD foodmenu.csv .

CMD ["python", "./main.py", "./eaterlog1.csv", "./foodmenu.csv"];

#CMD ["python", "./test.py"]