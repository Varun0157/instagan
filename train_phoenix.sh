python train.py --dataroot /scratch/varun.edachali/shp2gir_coco --model insta_gan --name shp2gir_scratch --loadSizeH 220 --loadSizeW 220 --fineSizeH 200 --fineSizeW 200 --display_id 0 --display_freq 10000 --verbose --batch_size 1 --gpu_ids 2

# 3rd gpu because it's usually less occupied in phoenix 
# display_id 0 ensures they do not try to serve to a port 
# display_freq 10000 ensures that the display is not called at all (not really required though)
