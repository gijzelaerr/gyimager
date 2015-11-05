On Jake for now compile with:

```
python setup.py build_ext -I/usr/include/casacode:/usr/include/casacore:/build/lofar-2.12.1/CEP/Imager/AWImager2/include
```

We need to set the casacode and casacore include paths, since the AWimager2 headers need this. We for now compile against the lofar source headers, since not all headers all correctly installed (fixed in trunk).

Now install it (in a virtualenv):

```
pip install .
```

The library paths in the lofar logic are hardcoded to the Red Hat way of, so before usage you need to run:

```
export LD_LIBRARY_PATH=/usr/lib64
```

If you want to manually compile the lofar tree, don't forget to supply the CASAREST_ROOT_DIR to enable the compilation of AWImager2:

```
cd <lofarsource>
mkdir build/gnu_opt
cd build_gnu_opt
cmake ../..  -DCASAREST_ROOT_DIR:PATH=/usr/include/casarest -DBUILD_PACKAGES="Offline" -DCASA_ROOT=/usr
```


