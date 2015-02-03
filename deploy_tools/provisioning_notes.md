Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:
    
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|
-- sites
   |
   -- SITENAME
      |
      |-- database
      |
      |-- source
      |
      |-- static
      | 
      |-- virtualenv



## Notes on using the fabric script (fabfile.py)
After the automatic deployment, the nginx configuration have to 
be done properly in order to get the site running on the server

* Create sites-available file for the nginx from the template
sed "s/SITENAME/YOUR_SITE_NAME/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/YOUR_SITE_NAME

* Create a link to the sites-available in the sites-enabled
sudo ln -s /etc/nginx/sites-available/YOUR_SITE_NAME /etc/nginx/sites-enabled/YOUR_SITE_NAME

* Write Gunicorn upstart script (copy the template like above)

* Finally start both services
sudo service nginx reload
sudo start gunicorn-YOUR_SITE_NAME

!!!!!!!! IMPORTANT !!!!!!!!
In the current version of the templates there is also a variable USERNAME
that shall be replaced too - DO NOT FORGET THAT
TODO: Add a description how to replace this variable also

!!! IMPORTANT !!! In the current version there is also a variable USERNAME !!!
TODO: Also replace the USERNAME
