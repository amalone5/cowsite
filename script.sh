#!/bin/bash

echo '' > /var/www/html/index.html
echo '<p>' >> /var/www/html/index.html
fortune >> /var/www/html/index.html
echo '</p>' >> /var/www/html/index.html

