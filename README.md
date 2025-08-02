# Bone-fracture-detector
An end-to-end deep learning project for detecting bone fractures from X-ray images with 98.07% accuracy, deployed as a Flask web application.                      
Built using Python, TensorFlow, Keras, OpenCV, and Flask.                                          
This project follows the Data Ingestion → Transformation → Storage → Analysis/Output → Deployment pipeline:                                          

1️⃣ Data Ingestion                                         
Loaded 4,900+ labeled medical X-ray images from structured folders (train, test, val).                                 
Used Python's os module and custom data() function to read file paths and class labels into Pandas DataFrames.                                    
                                           
2️⃣ Data Transformation                                      
Preprocessed images using OpenCV and ImageDataGenerator:                                 
Resized to (224, 224) pixels.                                       
Rescaled pixel values to [0, 1].                                       
Applied data augmentation (rotation, zoom, flipping) for better generalization.                                   
Encoded labels for binary classification (fracture vs. no fracture).                         
                                       
3️⃣ Data Storage                                          
Maintained structured directories for training, validation, and testing.                           
Stored processed image paths and labels in DataFrames for reproducibility.                                      
                                       
4️⃣ Analysis & Model Training                                
Designed a Convolutional Neural Network (CNN) architecture:                           
3 convolutional blocks with Batch Normalization and MaxPooling.                                         
Fully connected layers with Dropout for regularization.                                      
Achieved 98.07% test accuracy.                                          
Evaluated performance with:                                                               
Confusion Matrix                                           
Classification Report                                            

5️⃣ Deployment                                          
Integrated trained model into a Flask web application.                                    
Users can upload an X-ray image and get real-time fracture detection results.                                           
![image](https://github.com/user-attachments/assets/3be79932-5640-4251-8207-e13dc32dba75)
![Uploading image.png…]()
