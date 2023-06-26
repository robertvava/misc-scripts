def collate_images_dataset(idx_val, reduce = False, limit_samples = False, data_dir = '/eeg_dataset', transforma = None):

    import os
    from PIL import Image
    from torchvision import transforms
    from tqdm import tqdm


    transformation = transforms.Compose([
        transforms.Resize((128,128)),
        transforms.ToTensor()
        ])

    img_dirs = os.path.join(os.getcwd() + data_dir, 'images', 'training_images')

    image_paths = []
    for root, dirs, files in os.walk(img_dirs):
        for file in files:
            if file.endswith(".jpg"):
                image_paths.append(os.path.join(root,file))
                
    image_paths.sort()

    if reduce: 
        reduced = []
    train = []
    val = []
    for i, image in enumerate(tqdm(image_paths, desc = 'Training and validation images loading...')):
        if idx_val[i] == True:
            img = Image.open(image).convert('RGB')
            img = transformation(img)
            val.append(img)
        elif reduce:
            if limit_samples[i] == True: 
                img = Image.open(image).convert('RGB')
                # img = transformation(img)
                reduced.append(img)
        else:
            img = Image.open(image).convert('RGB')
            # img = transformation(img)
            train.append(img)

        


    img_dirs = os.path.join(os.getcwd() + data_dir, 'images', 'test_images')

    image_paths = []

    for root, dirs, files in os.walk(img_dirs):
        for file in files:
            if file.endswith(".jpg"):
                image_paths.append(os.path.join(root,file))

    image_paths.sort()
    test = []
    for image in tqdm(image_paths, desc = 'Test images loading...'):
        img = Image.open(image).convert('RGB')
        img = transformation(img)
        test.append(img)

    if reduce: 
        return reduced, val, test
    
    return train, val, test