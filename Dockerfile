FROM postgres

# Switch to root to perform tasks
USER root

# Create directories with correct permissions and ownership
RUN mkdir -p /var/run/postgresql && chown -R postgres:postgres /var/run/postgresql && chmod 777 /var/run/postgresql \
    && mkdir -p /var/lib/postgresql && chown -R postgres:postgres /var/lib/postgresql && chmod 777 /var/lib/postgresql

# Switch back to the postgres user
USER postgres

# Set environment variables
ENV POSTGRES_DB Clinc
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD database
ENV PGPORT 5432