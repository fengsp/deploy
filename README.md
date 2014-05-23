deploy
======

Deploying with Fabric

Future
------
* virtualenv
* static support
* more feature
* prompt

Usage
-----

Remember to adjust supervisord.conf, modify you app location and gunicorn config fire location, it should be `/web/projectname`

    $> fab install # Use this for your first deployment
    $> fab upgrade # Use this for your later upgrades
