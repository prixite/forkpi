FROM nginx:1.17.6-alpine

RUN apk update \
    && apk add --no-cache openssl \
    && mkdir /etc/nginx/ssl

# Generate self signed certificate
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
	-keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt \
	-subj "/C=US/ST=CA/L=SF/O=MyOrg/OU=MyApp/CN=localhost"

COPY nginx.conf /etc/nginx/conf.d/default.conf
