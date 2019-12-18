import sys
from statistics import mean

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print("Processing input file: {input_file_path}")

    with open(input_file_path) as f:
        for line in f:
            avgset = line[:-1].split(',')
            avgset = set(map(float, avgset))
            avg = mean(avgset)
            print(avg)

if __name__== "__main__":
    main()
