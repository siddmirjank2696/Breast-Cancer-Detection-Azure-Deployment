# An application that detects whether a patient has Breast Cancer or not. By following the steps below, users can run this application

### 1. Clone this repository.
```
git clone https://github.com/siddmirjank2696/Breast-Cancer-Detection-Azure-Deployment.git
```

### 2. Install Docker from the [official docker website](https://docs.docker.com/get-docker/). Click on the download link for your specific operating system.

### 3. Open terminal and change the path to the path of this repository.

### 4. Build a docker image using the following command. [IMAGE_NAME] can be any user defined name given to the image.
```
docker build -t [IMAGE_NAME] .
```

### 5. Run the docker image on your localhost at port 4001. Here, [IMAGE_NAME] should be the exact same name you gave the image during building it.
```
docker run -p 4001:4001 [IMAGE_NAME]
```

### 6. Once you run the docker image, you can access the app at localhost:4001 on your web browser.

### 7. Once the app is running, Type an input in the provided box. The input should be 30 values separated by commas. You can manually add these 30 input values, or you can copy values from the input files malignant.csv and benign.csv provided in the repository. Each line in these files corresponds to one set of 30 input values. 

### 8. This app will predict whether the tumor is malignant or benign depending on the input values provided by the user.