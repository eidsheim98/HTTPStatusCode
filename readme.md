# HTTPStatusCode

Ever wondered what that nasty HTTP statuscode you just got back means? Tired of looking it up every single time? 
Look no further. HTTPStatusCode is a simple program that lets you look this up inside the terminal. The code 
descriptions are retrieved from https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

## Installation

### Windows

Start by cloning this repository into a desired folder. To run the program from anywhere in the terminal, 
I would recommend creating a specific folder i an easy-to-remember location you would not need administrative
rights to edit. This could for instance be in a folder called

```bash
C:/Users/{username}/.cmd
```

Go into this directory using the command

```bash
cd C:/Users/{username}/.cmd
```

Then run the command for cloning the repository

```bash
git clone https://github.com/eidsheim98/HTTPStatusCode.git
```

Next, add this folder to path, to be able to run the file from anywhere on the computer

```bash
set PATH=%PATH%;C:/Users/{username}/.cmd
```

After this, change directory into HTTPStatusCode

```bash
cd HTTPStatusCode
```

The last step is to run the setup.py file

```bash
python setup.py
```

If no errors are encountered, you are good to go!

### Linux

Linux support is currently in development


## Usage

You run the script by typing 

```bash
hs {statuscode}
```

That means that if the code you got is 404, you should write

```bash
hs 404
```

And that should give you this information:

```bash
Statuscode:     404
Message:        Not Found
Type:           Client Error Message
Description:    The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
