import glob
import sys

if __name__=="__main__":
    try:
        dirpath = sys.argv[1]
        csvfiles = []
        for filename in glob.glob(dirpath+"/**/*.csv"):
            csvfiles.append(filename)
        print(csvfiles)
    except IndexError, e:
        print("usage error: \n correct usage=> python get-csv-files.py $path_to_csvdir")
