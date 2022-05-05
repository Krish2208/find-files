## Find Files

A Python Package to find files which contain a specific string.

**Installation**

> **Python>=3.7 is required**

    git clone https://github.com/Krish2208/find-files
    cd find-files
    pip install .

---

**Examples**

    from findFiles import find
    # find.find(key, in_directory=None, out_directory=None)


    find.find("covid")
    # This will search "covid" in the files present in the
    # current directory and will extract all the files which
    # contains the word in a "./result%d%m%Y_%H%M%S" sub-directory.


    find.find("covid", in_directory="E:/test")
    # This will search "covid" in the files present in the
    # specified in in_directory and will extract all the files which
    # contains the word in a "./result%d%m%Y_%H%M%S" sub-directory.

In a similar way, one can use the "out_directory" to specify the folder where files are to be extracted.
