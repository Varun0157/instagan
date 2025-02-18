# Notes 
- check `--continue_train`. Using a pre-trained model as init could also lead to better results on raw InstaGAN. 
- 

# Plan 
- create a separate model that only operates on masks - use the code from `InstaGanModel.py` as the basis, just alter args to `define_G` and such. 
- make said model an attribute of InstaGAN, which now passes encoded "correct" masks as input during the forward pass of the generator. 

- train separately, then pass as a param and initialise InstaGanModel. Then, we only really need the netG_A's of the segmodel and don't need to worry about set input and such, perhaps. 

