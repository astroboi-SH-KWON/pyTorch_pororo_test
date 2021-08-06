# pyTorch_pororo_test
astroboi_pytorch : pytorch 1.6.0, torchvision 0.7.0, fairseq 1.0.0, pororo 0.4.2

manual : https://kakaobrain.github.io/pororo/index.html
git : https://github.com/kakaobrain/pororo


    how to make pororo env
        1. conda create -n astroboi_pytorch python=3.8
        2. conda activate astroboi_pytorch
        3. conda install pytorch==1.6.0 torchvision==0.7.0 -c pytorch  
            # pororo supports only pytorch 1.6.0
        4. git clone https://github.com/pytorch/fairseq
            cd fairseq
            pip install -e ./
        5. pip install pororo
        6. done... but recheck pytorch version is still 1.6.0

    extra libs
        cv2(opencv) for ocr : conda install -c conda-forge opencv
        skimage for ocr : conda install -c anaconda scikit-image

