## Changes Made
- seg masks for val set in `ccp` dataset
- fix inference and training errors in `unaligned_seg_dataset`
- fix multi-batch single-gpu code (`ResNetSetGenerator` not configured for multiple batches) **with the assumption of single instance masks per image**.
- scripts to convert image directories into datasets of the expected format 
- and more...

refer to branches for variants of the model. `master` has been polluted with experimentation. 

*NOTE*: the project is still a WIP. 

