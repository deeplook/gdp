# gdp

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/deeplook/gdp/rust_kernel?urlpath=lab)

Building a Jupyter Rust kernel, see https://lib.rs/crates/evcxr_jupyter

```
conda install -y -c conda-forge rust
cargo install evcxr_jupyter # doesn't compile
chmod +x ~/.cargo/bin/evcxr_jupyter
~/.cargo/bin/evcxr_jupyter --install
```

Fails with: 

```
error: failed to compile `evcxr_jupyter v0.4.2`, intermediate artifacts can be found at `/tmp/cargo-install9VX8AG`
```
