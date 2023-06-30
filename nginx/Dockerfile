FROM nginx:1.17.6

RUN apt update \
    && apt install -y openssl \
    && mkdir /etc/nginx/ssl

# Generate a configuration file for openssl
COPY openssl.cnf /etc/nginx/ssl/openssl.cnf

# Generate private key
RUN openssl genrsa -out /etc/nginx/ssl/nginx.key 2048

# Create certificate signing request
RUN openssl req -new -key /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.csr -subj "/C=US/ST=CA/L=SF/O=MyOrg/OU=MyApp/CN=localhost" -config /etc/nginx/ssl/openssl.cnf

# Generate the certificate
RUN openssl x509 -req -in /etc/nginx/ssl/nginx.csr -signkey /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt -days 365 -extensions v3_ext -extfile /etc/nginx/ssl/openssl.cnf

COPY nginx.conf /etc/nginx/conf.d/default.conf
