# gdp

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/deeplook/gdp/rust_kernel?urlpath=lab)


## Not working

Building a Jupyter Rust kernel, see https://lib.rs/crates/evcxr_jupyter

```
sudo apt install libzmq3-dev
conda install -y -c conda-forge rust
cargo install evcxr_jupyter # doesn't compile in rust_kernel branch
chmod +x ~/.cargo/bin/evcxr_jupyter
~/.cargo/bin/evcxr_jupyter --install
```

##  Working

https://github.com/google/evcxr/blob/master/binder/postBuild

```
sudo apt install libzmq3-dev
curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain=stable -y
~/.cargo/bin/cargo install evcxr_jupyter
chmod +x ~/.cargo/bin/evcxr_jupyter 
~/.cargo/bin/evcxr_jupyter --install
```
