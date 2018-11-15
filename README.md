## ZIP Shotgun

TODO Add description

https://blog.silentsignal.eu/2014/01/31/file-upload-unzip/
https://www.owasp.org/index.php/Test_Upload_of_Malicious_Files_(OTG-BUSLOGIC-009)
https://github.com/WhiteWinterWolf/wwwolf-php-webshell

#### Installation

```pip install zip-shotgun```

#### Usage and options

```
Usage: zip-shotgun [OPTIONS] OUTPUT_ZIP_FILE

Options:
  --version                       Show the version and exit.
  -c, --directories-count INTEGER
                                  Count of how many directories to go back
                                  inside the zip file (e.g 3 means that 3
                                  files will be added to the zip: shell.php,
                                  ../shell.php and ../../shell.php where
                                  shell.php is the name of the shell you
                                  provided or randomly generated value
                                  [default: 15]
  -n, --shell-name TEXT           Name of the shell inside the generated zip
                                  file (e.g shell.php). If not provided it
                                  will be randomly generated
  -f, --shell-file-path PATH      A file that contains code for the shell. If
                                  this option is not provided wwwolf
                                  (https://github.com/WhiteWinterWolf/wwwolf-
                                  php-webshell) php shell will be added
                                  instead. If name is provided it will be
                                  added to the zip with the provided name or
                                  if not provided the name will be randomly
                                  generated.
  --compress                      Enable compression. If this flag is set
                                  archive will be compressed using DEFALTE
                                  algorithm with compression level of 9. By
                                  default there is no compression applied.
  -h, --help                      Show this message and exit.
```

#### Examples

TODO
