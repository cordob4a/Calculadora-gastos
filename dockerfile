FROM postgres:16

ENV POSTGRES_DB=gastos_db
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin123

COPY init.sql /docker-entrypoint-initdb.d/
