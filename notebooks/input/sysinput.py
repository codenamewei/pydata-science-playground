
import sys



if __name__ == "__main__":

    print(f"Length of sys.argv: {len(sys.argv)}")
    print(sys.argv[0])

    if len(sys.argv) >= 2:

        print(type(sys.argv[1]))
        print(sys.argv[1])
    