# CSG6-Car_Price_ML
## Project : Car Price Prediction 

## Overview
Car Price Prediction Machine learning model is used to create one of the core features of easyMoney which is used to test how much it gonna
work and serve our user well before we work on price prediction on all kind of product categories in our platform  

The main reason for choosing Car to work first ,as we have worked on data wrapping on Khmer24 Website together with a short conversation with 
Mr.Rady the CEO of Khmer 24 whom is our reference , has mentioned that Car , Real Estate , and Smart Phone 

## Requirements 

If you do not have Python installed yet, it is highly recommended that you install the Anaconda distribution of Python, which already has the below 
packages and more included.

You will also need to have software installed to run and execute a Jupyter Notebook.If you do not have Python installed yet, it is highly recommended
that you install the Anaconda distribution of Python, which already has the above packages and more included.Make sure that you select the Python 
3.x installer.

link : conda install -c conda-forge jupyterlab

This project requires Python 3.6 and the following Python libraries installed:

. Flask==1.1.2
. Werkzeug==1.0.1
. Jinja2>=3.0
. click>=7.1.2
. itsdangerous>=2.0
. MarkupSafe>=2.0
. requests==2.22.0
. pandas==1.3.3
. config==0.5.1
. waitress==2.0.0
. gunicorn==20.1.0
. scikit-learn==0.24.2
. numpy==1.20.1

Our you can instll the requirements.txt file to have these libraries installed quickly 
link: pip install -r requirements.txt

## Data 
We do get this dataset from Kaggle with the size file 1.3GB 
Our ML model will require customer informations, such as:
. price
. year
. manufacturer
. model
. cylinder
. fuel
. kms_driven
. status
. transmission
. drive_wheel
. body_type
. colour

## Code
Template code is provided the file with the extension "ipynb" car_price_prediction_1.ipnb notebook file for our model testing on notebook 
but since we have already deployed our model , that we convert it into "pickle" file that we exported as our ML model so there is no need to run the . 
You are not re to use the included vehicles.csv dataset file to run you wish to work in in localhost.But since we have already 
deployed our "model" on AWS.

While some code has already been implemented to get you started, you will need to implement additional functionality when requested to successfully
complete the project. after you have done you need python main.py to run the our project.

------- On local Host ------- 
So what you have to do next is 
running main.py using cmd 
flask run to run the localhost 

### Last But Not Least 
run custom_index.html file 
and play around with it by filling up the required information .


------- Remark ------- 
Since this web application is designed to test our ml model in localhost only , for the main api and the real process is designed 
on our mobile applicaiton and web application 

Thanks




