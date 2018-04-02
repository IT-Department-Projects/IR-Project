# ImageFind

## About

ImageFind is a Search Engine for Data Driven Diagrams that it is able to “expand” queries to include not only exactly matching diagrams, but also diagrams that are likely to be related in terms of their production pipelines. We demonstrate the resulting search system by indexing over 500 images pulled from various datasets.

## Contributors
* [Salman Shah](https://github.com/salman-bhai)
* Aiman Abdullah
* Rashika Chowlek
* Adwaith G.

## Documentation

* Documentation for the same can be found on the Project Wiki.

## Environment Setup

* It is preferable if you use Python Ananconda Environment. You can download it from [here](https://www.anaconda.com/download/#linux)

* Create a new conda environment using the following command:
```
conda create -n image-find python=3.5
```

* Activate the environment by running the following code:
```
source activate image-find
```

* To install the required libraries, run the following commands:
```
conda install numpy pandas nltk matplotlib reportlab
```

To view all the dependencies, check out the [requirements](requirements.txt) file.

## Running the Code

The basic usage is `python VSM.py`.
