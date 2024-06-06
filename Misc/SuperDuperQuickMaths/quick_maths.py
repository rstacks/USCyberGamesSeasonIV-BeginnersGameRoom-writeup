import subprocess

# Run provided nc command
with subprocess.Popen(["nc", "0.cloud.chals.io", "15072"],
  stdin=subprocess.PIPE, stdout=subprocess.PIPE) as process:
  
  # Read and evaluate input
  while True:
    math_problem = process.stdout.readline()
    print(math_problem)

    # Evaluate the math problem
    math_solution = ""
    try:
      math_solution = str(eval(math_problem))
    except:
      continue

    # Send results
    process.stdin.write(math_solution.encode())
    process.stdin.flush()
