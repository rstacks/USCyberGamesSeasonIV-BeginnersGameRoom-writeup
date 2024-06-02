We are provided with an executable called rev. I uploaded this file to the decompiler explorer at
dogbolt.org and selected the output of Hex-Rays. We can see the main() function of the program near the
end of the decompiler output. Here, we see that the program accepts input for the flag and checks it
with a function called sub_11A9(), which is defined just above main(). From this function, we learn that
the flag is exactly 22 characters long and can be constructed by doing a bitwise XOR on each pair of
elements (with matching indices) in the byte_4050 and byte_4070 arrays. These two arrays are defined at the
top of the Hex-Rays output.

With this information, I wrote a Python script to create an array of the values resulting from performing
XOR on each pair of elements from byte_4050 and byte_4070 (named lst1 and lst2 in my script, respectively).
I then converted each of these values to their ASCII characters, which yielded the flag.

flag: SIVBGR{x0r_B@s1cs_R3v}
