# gdp

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/deeplook/gdp/multikernels?urlpath=lab)

## C++

```
conda install -c conda-forge xeus-cling
```

## Julia

```
conda install -c conda-forge julia
julia -E 'using Pkg; Pkg.add("IJulia")'
```

## JVM

```
conda install -c conda-forge ipywidgets beakerx
```

## Lua

```
conda install -c conda-forge lua luarocks
pip install ilua
```

## Octave

```
sudo apt install octave
sudo apt install octave-symbolic
sudo apt install octave-miscellaneous
sudo apt install gnuplot
sudo apt install ghostscript
conda install -c conda-forge octave_kernel
```

## Rust

https://github.com/google/evcxr/blob/master/binder/postBuild

```
sudo apt install libzmq3-dev
curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain=stable -y
~/.cargo/bin/cargo install evcxr_jupyter
chmod +x ~/.cargo/bin/evcxr_jupyter 
~/.cargo/bin/evcxr_jupyter --install
```
