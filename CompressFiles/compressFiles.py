import tarfile
import os.path

# Function which takes in the the output name and the source of the file to compress
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        # Loop while files are added into the compressed file
        for files in source_dir:                                    
            tar.add(files, arcname=os.path.basename(files))
    tar.close()

if __name__ == '__main__':
    listOfFiles = []
    
    # Take input of files that you want to compress
    while (True):
        name = input("Enter file name or press enter to exit: ")

        if not name:
            break
        else:
            listOfFiles.append(name)

    # Send the files to the function for compression
    make_tarfile("compressedFiles.tar.gz", listOfFiles)