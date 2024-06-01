We are provided with a binary. I uploaded it to the Decompiler Explorer at dogbolt.org. Here, I took
note of two decompilation outputs: the one provided by BinaryNinja the one provided by Hex-Rays. The
BinaryNinja output provided the most readable C code of all the decompilers. By examining the main()
function, we can see that this program is using a function called checkflag() to verify a
user-provided flag. If we can figure out how to get checkflag() to return true, then we can find
the flag. Within the checkflag() function, we can see that the flag is 31 characters long. There also
seems to be a string within the program called flagCheck. In order for checkflag() to return true,
the sum of the ASCII value of a given character in flagCheck and the corresponding character in our
input must be 128 for every pair of characters. In other words, if we know the ASCII values of
flagCheck's characters, then we can subtract each of them from 128 to get the ASCII values of the
flag. Unfortunately, BinaryNinja was not able to get the value of flagCheck, which is why we are
also considering the decompilation output of Hex-Rays. Near the top of Hex-Rays's output is an array
of integers, which represents the ASCII values of flagCheck. We now have all the information we need.
I wrote a quick Python script to loop over the array from Hex-Rays and subtract each of its
elements from 128. Then, I converted those values into ASCII characters. This yielded the flag.

flag: SIVBGR{v3ry_d1ff1cult_passw0rd}
