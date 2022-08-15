import sys
"""
python sysarg.py 100 200
"""

if __name__ == "__main__":
    
    for i in range(1, len(sys.argv)):
        
        print(f"{i}: {sys.argv[i]} of type {type(sys.argv[i])}")