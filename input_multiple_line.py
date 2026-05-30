print("Enter your input (press Ctrl+D or Ctrl+Z then Enter to finish):")

# Accepting multiple lines until EOF (End of File)
import sys
for line in sys.stdin:
    print(line.strip().upper())
