We are told the flag is located in /flag.txt, but we cannot simply navigate to
https://uscybercombine-s4-parts-shop.chals.io/flag.txt. This website does, however, allow us to add
new content to it (new parts). This gave me the idea to intercept the HTTP requests and modify them.
Burp Suite on my Kali Linux VM is perfect for this. I navigated to the page on the website where we
can create new blueprints (https://uscybercombine-s4-parts-shop.chals.io/blueprint). I entered in
some random information for each text box, then clicked Create. I intercepted the request with Burp
Suite. This was, fittingly, a POST request. The website interfaces with XML files to create the
parts list. I modified the XML for the blueprint I just created. I added a DOCTYPE declaration and
defined an entity "the_flag," which would contain the contents of /flag.txt. I then changed the
"name" component of my blueprint to &the_flag; in order to print the flag once the page loaded.
With the payload ready, I forwarded the request to the website, and the flag was revealed once
the page loaded.

flag: SIVBGR{fu11y_upgr4d3d}
