# Practical introduction of numerical analysis applied on images

Small university project proposed in the subject "Numerical Analysis" in the 1st year of MSc of Computer Science in Imaging & Machine Learning at the University of Caen Normandy in order to to implement some mathematical equations on 2-dimensionnal images seen in this course.

## Table of contents

  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Setup](#setup)
  - [Commands](#commands)
  - [Results](#results)
  - [Authors](#authors)
  - [License](#license)

## Introduction

The goal of the project is to implement some mathematical equations on 2-dimensionnal images :

- the dilation equation :

<p align="center">
    <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_white&space;\large&space;\left\{\begin{matrix}&space;\frac{\partial&space;f(u,t)}{\partial&space;t}&space;&&space;=&space;&&space;+&space;|\nabla_w^{+}&space;f(u,t)|_{\infty}&space;\\&space;f(u,0)&space;&&space;=&space;&&space;f_0(u)&space;\\&space;\end{matrix}\right." title="\large \left\{\begin{matrix} \frac{\partial f(u,t)}{\partial t} & = & + |\nabla_w^{+} f(u,t)|_{\infty} \\ f(u,0) & = & f_0(u) \\ \end{matrix}\right." />
</p>

- the erosion equation :

<p align="center">
    <img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_white&space;\large&space;\left\{\begin{matrix}&space;\frac{\partial&space;f(u,t)}{\partial&space;t}&space;&&space;=&space;&&space;-&space;|\nabla_w^{-}&space;f(u,t)|_{\infty}&space;\\&space;f(u,0)&space;&&space;=&space;&&space;f_0(u)&space;\\&space;\end{matrix}\right." title="\large \left\{\begin{matrix} \frac{\partial f(u,t)}{\partial t} & = & - |\nabla_w^{-} f(u,t)|_{\infty} \\ f(u,0) & = & f_0(u) \\ \end{matrix}\right." />
</p>

## Setup

You need to have Python 3 installed on your machine.
You can install the dependences with one of this two commands :
```sh
# if you already have installed virtual environment
$ pipenv install
$ pipenv shell
```
or
```sh
$ pip3 install -r requirements.txt
```

## Commands
To launch the script, you only have to execute this command :
```sh
$ python3 script.py
```

## Results
From this image :
<p align="center">
    <img src="image.jpg" />
</p>
- if you dilate the image :
<p align="center">
    <img src="dilated_image.png" />
</p>
- if you erode the image :
<p align="center">
    <img src="eroded_image.png" />
</p>

## Authors
- [LETELLIER Guillaume](https://github.com/Guigui14460)

## License
Project under the MIT license.