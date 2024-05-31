We are provided with a eml file. I used the website https://www.emlreader.com to read this file and
get its attachments. Within the email is a file called evidence.zip, which I downloaded. At the end
of the email is a string of hexadecimal numbers that represent the password needed to unzip the
evidence (53 65 63 75 72 65 5f 43 6f 64 65 3a 4f 72 64 65 72 5f 36 36). I converted these numbers
to their ASCII characters, which yielded the following string: "Secure_Code:Order_66." I unzipped
the evidence and provided that string as the password. Within the zip archive was a file called
evidence.txt, which contains the flag.

flag: SIVBGR{th3_ev1d3nc3_1s_h3r3}
