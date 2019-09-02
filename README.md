# gdp

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/deeplook/gdp/multikernels?urlpath=lab)

## Kernels

**C++**

```
conda install -c conda-forge xeus-cling
```

**Julia**

```
conda install -c conda-forge julia
julia -E 'using Pkg; Pkg.add("IJulia")'
```

**JVM (Clojure, Groovy, Java, Kotlin, Scala)**

```
conda install -c conda-forge ipywidgets beakerx
```

**Lua**

```
conda install -c conda-forge lua luarocks
pip install ilua
```

**NodeJS**

```
sudo apt-get install nodejs-legacy npm ipython ipython-notebook
sudo npm install -g ijavascript
ijsinstall
```

**Octave**

```
sudo apt install octave
sudo apt install octave-symbolic
sudo apt install octave-miscellaneous
sudo apt install gnuplot
sudo apt install ghostscript
conda install -c conda-forge octave_kernel
```

**Processing**

```
pip install calypso_processing
wget http://download.processing.org/processing-3.5.3-linux64.tgz
tar xvf processing-3.5.3-linux64.tgz
echo 'export PROCESSING_JAVA=$HOME/processing-3.5.3/processing-java' >> .profile
python3 -m calysto_processing install --user
```

**R**

Installed by [mybinder.org](https://mybinder.org) using the files `install.R` and `runtime.txt`.


**Rust**

https://github.com/google/evcxr/blob/master/binder/postBuild

```
sudo apt install libzmq3-dev
curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain=stable -y
~/.cargo/bin/cargo install evcxr_jupyter
chmod +x ~/.cargo/bin/evcxr_jupyter 
~/.cargo/bin/evcxr_jupyter --install
```

**Spark (PySpark, Spark, SparkR)**

```
conda install -c conda-forge pyspark
conda install -c conda-forge sparkmagic
```
