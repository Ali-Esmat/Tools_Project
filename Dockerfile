FROM postgres

ENV POSTGRES_DB Clinc
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD database
# Customize the permission settings
USER root
RUN mkdir -p /var/lib/postgresql/data/custom-data && chown -R postgres:postgres /var/lib/postgresql/data/custom-data
USER postgres

CMD["postgres","-c","config_file=/var/lib/postgresql/data/custom-data/postgresql.conf"]