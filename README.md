# MOTHe
Mothe is a pipeline developed to detect and track multiple objects in a heterogeneous environment. MOTHe is based on a simple
Convolutional neural network and allows users to generate training data using a simple GUI tool, automatically        detects 
classified objects and tracks them. MOTHe is designed to be generic which empoweres the user to track      any
objects of interest in a natural setting. 

__MOTHe has been developed and tested on Ubuntu 16.04 using python 3.5.2__
# PIPELINE DESCRIPTION:

The MOTHe repository includes 5 folders and 5 excecutables dedicated to the following classes.

1. __System configuration__: The system configuration is used to setup MOTHe on the users system. Basic details such as the path to 
   the local repository, path to the video to be processed, the size of the individial to be cropped and the size of the bounding
   box to be drawn during the detection phase. It also contains a shell script which will automatically install the correct versions
   of the required python modules on the users system. 

2. __dataset generation__: The dataset generation is a crucial step towards object detection and tracking. The manual effort required 
   to generate the required amount of training data is huge. The data generation class and executable highly automates the process
   by allowing the user to crop the region of interest by simple clicks over a GUI and automatically saves the images in appropriate
   folders. It is important however to crop the images consistantly since the accuracy of the classifier plays a huge role in the 
   overall efficiency of the pipeline.
   
3. __Training the convolutional neural network__: After generating sufficient number of training example, the data is used to train the
   neural network. The neural network produces a classifier as the output. The accuracy of the classifier is dependent on how well 
   the network is trainied which in turn depends on the quality of data generation. The various tuning parameters of the network is 
   fixed to render the process easy for the users. This network has proven its efficiency when it comes to binary classification 
   (object of interest and background). Multi-class classification is not supported on this pipeline.

4. __Object detection__: The weights produced by the trained network is used to classify various regions of the test frame. In the event
   of a positive classification, a square bounding box is drawn around that region annotating the object. Using methods like sliding 
   window helps to cover an entire frame for region proposal but is computationally expensive. MOTHe employs the thresholding technique
   to identify the potential object of interest to be classified. This method allows us to utilize finite number of points around which 
   the region is classified making it an efficient and fast process. The object detection phase of MOTHe provides the user with a csv
   file containing the coordinates of all positive classifications and a video file with the detected objects with bounding boxes.
   
5. __Object tracking__: Object tracing is the final goal of the MOTHe. The csv stored during the object detection stage is utilized for the 
   detected keypoints and unique ids are generated for all the detected objects. The ids are tracked through frames of the test video 
   based of the distance between the keypoints during subsequent frames. Few objects that go undetected however are reassigned with a new
   id. Additionnal individuals entering the frame are assigned a new id right after detection.
   
 # USAGE
 
 __MOTHe flowchart__
 
 <br>
 <img height="700" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/flowchart_mothe.jpg">
 <br>
 
 The flowchart depicts the order of the functions to be used in MOTHe. The user should follow the following steps to successfully
 detect and track multiple objects using MOTHe
 

 
 # JUPYTER NOTEBOOK IMPLEMENTATION (Cross-platform)
 
The usage of MOTHe requires certain packages to be installed on your ubuntu machine. A mothe.sh shell script is provided which helps in 
the installations of these packages in a single step. Open your terminal change the directory to the mothe directory.
 
 
To get started with MOTHe, you need to have a copy of the MOTHe git repository on your local machine.
Open the terminal and use the 'git clone' command to clone the MOTHe repository as shown in the figure below. You can also download the MOTHe repository directly from the github page.

**_git clone https://github.com/BinaryConcussion/MOTHe/_**

<br>
<img height="350" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/clone_mothe.png">
<br>

After downloading the repository on the local system, open the terminal and navigate to the local MOTHe directory 
as shown below.

**_cd MOTHe_**
            
<br>
<img height="350" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/change_directory.png">
<br>


The usage of MOTHe requires certain packages to be installed on your ubuntu machine. A mothe.sh shell script is provided which helps in 
the installations of these packages in a single step. List the files in the MOTHe directory and take note of the 'mothe.sh' file

**_ls_**

<br>
<img height="350" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/mothe_content.png">
<br>

To use the mothe.sh script, you have to first change the permissions to the file using the following command

**_chmod +x ./mothe.sh_**

<br>
<img height="350" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/chmod.png">
<br>

After changing the permissions to the mothe.sh file, use the bash command to use the shell script as shown below

**_sudo bash mothe.sh_**

<br>
<img height="350" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/bashmoth.png">
<br>

The mothe.sh also installs and configures a virtual environment where an environment can be created specific to MOTHe. Create a virtual environment
by the name of mothe as shown below

**_mkvirtualenv mothe -p python3_**

<br>
<img height="350" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/mkvir.png">
<br> 

After creating the the virtual environment, activate the virtual environment as follows

**_workon mothe_**

<br>
<img height="350" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/workon.png">
<br> 

After activating the mothe environment, configure all python modules using the requirement.txt as follows

**_pip install -r requirement.txt_**
          
<br>
<img height="350" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/reqpip.png">
<br>

start the jupyter notebook by typing in 'jupyter notebook' in the terminal as shown below

**_jupyter notebook_**
            
<br>
<img height="350" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/start_jupyter.png">
<br>

The following screenshot is the jupyter notebook on the browser. Locate the 'mothe.ipynb' and click on it. Follow the instructions in the jupyter notebook.
            
<br>
<img height="500" src="https://github.com/Ananthsharma/MOTHe/blob/master/help_screenshots/jupyter_notebook.png">
<br>


 # LINUX IMPLEMENTATION 
 
 __Users may use the jupyter notebook implementation of MOTHe. The installations of libraries can be done with the 
 requirement.txt provided within the repository.__
 
 1. __Step 1__: Configure the system to install dependencies for MOTHe
 
    You may skip this step if you already have the modules installed or you are comfortable doing the installations manually.
    Multiple versions of the same module may cause errors. The use of a virtual environment is advisable to run MOTHe since the
    versions of the modules are specific. If you do not have the virtualenv and virtualenv wrapper installed, the configure.py
    script takes care of it automatically. Run the following code on the terminal to set up a virtualenv named mothe and install 
    all the required dependencies in it. (NOTE: No errors are expected on a fresh install of ubuntu 16.04. If there is an error with 
    excecuting this script, you may skip installing the virtual environment and install the dependencies on your system manually. If
    you prefer having a virtal environment, create a virtual environment using 'mkvirtualenv mothe' and install)
 
    **_python3 configure.py_**
    
    Argument: (required)
    _--dependencies_
 
 2. __step 2__: Activate the virtual environment 'mothe' (if you have it) and/or run the following code in the terminal
 
    **_workon mothe_**
 
    **_python configure.py_**
    
    Argument: (required)
    _--setup_mothe_
 
 3. __step 3__: To generate the training data, run the following code in the terminal. The step argument determines how many frames 
    to skip before cropping. This depends on the amount of data the user has (number of videos, length of videos and average number of 
    individuals in each frame). (Ex: A 20 second video with a frame rate of 30 fps has 600 frames in total. It is desirable to have about
    8000 to 10000 examples to train the neural network) 
 
    **_python generate_dataset.py_**
    
    Arguments:
    _--step_ (Number of frames to skip in the video for generating dataset)
 
 4. __step 4__: To train the neural network, run the following code in the terminal. The following code trains the neural network
    on default parameters. If you wish to change the parameters, arguments are provided
 
    **_python train_cnn.py_**
 
    Arguments:
    _--epochs_ (number of epochs for training)
    _--splitpct_ (Train-test-split ratio)
 
 5. __step 5__: For object detection, run the following code in the terminal
 
    **_python object_detection.py_**
 
 6. __step 6__: For object tracking, run the following code in terminal
 
    **_python object_tracking.py_**









 
 
 
 
 
 
 
