The title of this challenge hints that Alice and Bob are using Diffie-Hellman key exchange. We are provided with the
values of g, p, a, and b (12, 53, 8, and 67, respectively) after running the nc command. This allows us to
determine the value of the shared secret (note the figure on the Wikipedia article), which is 47. After entering
this value, we are provided with the encrypted flag and instructions on how to decrypt it. I copied the encrypted
text into CyberChef and added two operations to the recipe: first, "From Hex," and then "XOR" with a key of 47 in decimal.
This yielded the flag.

flag: SIVBGR{4_fl4g_fr0m_4l1c3_4nd_b0b}
