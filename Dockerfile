FROM postgres

ENV POSTGRES_DB Clinc
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD database

# Customize the permission settings
USER root
RUN chmod -R  777 /var/run/postgresql /var/lib/postgresql
USER postgres