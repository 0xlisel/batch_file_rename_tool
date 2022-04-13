import os
import logging
import argparse
from time import sleep
from progress.bar import Bar

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
parser = argparse.ArgumentParser(description="Batch file rename tool")

# positional arguments
parser.add_argument(
    "search",
    type=str,
    help="Search string for files to be renamed"
)

parser.add_argument(
    "replace",
    type=str,
    help="Replace string for files to be renamed"
)

# optional arguments
parser.add_argument(
    "-f",
    "--filetype",
    type=str,
    default=None,
    help="File type of files to be renamed (e.g. .txt)"
)
parser.add_argument(
    "-p",
    "--path",
    default=".",
    type=str,
    help="Path to the directory where the files will be renamed"
)

args = parser.parse_args()


def main():
    logging.info(f'Batch rename started in directory: {args.path}')

    # getting the values from args passed in command line and store in variables
    search = args.search
    replace = args.replace
    filetype = args.filetype
    path = args.path

    # get all contents in the directory given
    dir_contents = os.listdir(path)
    # logging.info(dir_contents)

    # create full paths by joining the path given with the doc name in dir_contents list
    file_paths = [os.path.join(path, doc) for doc in dir_contents]
    # logging.info(file_paths)

    # selecting only the files in the directory given
    dir_files = [doc for doc in file_paths if os.path.isfile(doc)]
    # logging.info(dir_files)

    # count of files renamed
    files_renamed = 0

    # loop through all files
    for doc in dir_files:

        # check if they match the search pattern
        if search in doc:

            # separate the doc name from the extension
            doc_full_path, ext = os.path.splitext(doc)

            # get just the doc direcory path without the doc name from doc path
            doc_dir_path = os.path.dirname(doc_full_path)

            # get just the doc name from the doc path
            doc_name = os.path.basename(doc_full_path)

            # check for filetype if any
            if filetype == ext or filetype is None:

                # replace just the doc name
                new_doc_name = doc_name.replace(search, replace)

                # the new doc path with the new doc name and extension
                new_doc_path = os.path.join(doc_dir_path, new_doc_name) + ext

                # rename the files
                os.rename(doc, new_doc_path)

                files_renamed += 1

                logging.info(f"Renamed file {doc} to {new_doc_path}")
                sleep(0.02)

    logging.info(f"Renamed {files_renamed} of {len(dir_files)} files")

if __name__ == '__main__':
    main()