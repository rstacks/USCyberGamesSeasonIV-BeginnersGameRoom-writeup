I opened Wireshark on my Kali Linux VM with the provided pcap file. This revealed a long list
of DNS queries. The challenge title and description suggest that an email is involved,
which most likely means it was encoded and sent covertly over DNS. I did notice that each
DNS query was made to an address that appeared to be encoded in some way. Within Wireshark,
I did Analyze->Follow->UDP Stream to get all of the DNS queries in one place. I then copied
the text and removed the periods, commas, and "x.meowcorp.cloud" strings, as these
didn't seem particularly important. The cleaned data is available in encoded_email.txt.
I then took the data to CyberChef and tried several decoding operations. Eventually, doing
a base32 decode revealed a fully readable email, which contained the flag.

flag: SIVBGR{wh0_n33ds_32_b4s3s}
