In addition to a link to the challenge website itself, we are also provided with the source
code for the website. After downloading and unzippping the provided files, I took note of two files:
main.py in the challenge directory and destroyer.py in the config directory. From main.py, we can see
that we can specify two variables in the website URL: command and arg. We can also see that if command
has the value "destroy_humans," then the website will run a shell script AND enter whatever we set
arg equal to into the terminal. This is begging to be exploited. I tested this vulnerability with the
following text at the end of the URL: /?command=destroy_humans&arg=;ls. Sure enough, I was able to see
the output of ls -- the contents of the website's working directory. 

Next, I examined the destroyer.py file. It seemed like this script would start a server on localhost
that listened for GET requests on port 3000. There were multiple options for paths to run a GET
request on, but the important option is /shutdown. The code implied that making a GET request to
/shutdown would reveal the flag. I needed to execute the following command on the website's server:
curl http://127.0.0.1:3000/shutdown. This would make the GET request I needed.

I combined what I just learned with the vulnerability discovered in main.py. I used
https://www.urlencoder.io to URL encode the command mentioned above. This was the final text
used at the end of the website URL:
/?command=destroy_humans&arg=%3Bcurl%20http%3A%2F%2F127.0.0.1%3A3000%2Fshutdown. The flag was revealed
on the resulting web page.

flag: SIVBGR{g00dby3_ARI4}
