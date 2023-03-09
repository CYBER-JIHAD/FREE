import os, sys
try:
    __import__("ox").menu()
except Exception as e:
    exit(str(e))
