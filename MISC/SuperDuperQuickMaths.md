We are given 50 simple math problems to solve, but each one must be solved within 3
seconds to get the flag. I'm not that good at mental math, so I wrote a Python script
to run the provided nc command and evaluate the math problems for me. I used the subprocess
module to run the nc command with the ability to read and write data. After connecting, I simply
read from stdout and used eval() to evaluate the math expression. I then sent the results to stdin.
This process repeated until all 50 problems were solved, which revealed the flag.

Note: I would avoid using eval() if you are accepting input from an untrustworthy source, as it
is very easy for an attacker to execute malicious code on the machine running the script.

flag: SIVBGR{L00kM0m!_ICANDO_m4th}
