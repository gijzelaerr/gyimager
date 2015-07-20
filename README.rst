for now comile with:

```
python setup.py build_ext -I/usr/include/casarest:/usr/include/casacore:lofar/CEP/Imager/LofarFT/include
```

Currently trying to get this to work with:

casacore 2.0.1
https://github.com/casacore/casacore/releases/tag/v2.0.1


casarest 1.3.1
https://github.com/casacore/casarest/releases/tag/v1.3.1


lofar 2.11.1
https://svn.astron.nl/LOFAR/tags/LOFAR-Release-2_11_1/


But it looks like the API for LofarFT changed.
