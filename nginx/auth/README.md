put your .htpasswd file here & run:
    
    htpasswd .htpasswd -c <username>

to add another to an existing file (-c overwrites existing), I run:
    
    htpasswd -n <username>

then copy-paste the command-line result into the existing .htpasswd file

[more here](https://httpd.apache.org/docs/2.4/programs/htpasswd.html)