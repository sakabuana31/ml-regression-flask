# ml-regression-flask

<div id="header" align="center">
  <img src="https://media.giphy.com/media/8qrrHSsrK9xpknGVNF/giphy.gif" width="200"/>
</div>

<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/sakabuana31/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" height="25px" alt="LinkedIn Badge"/>
  </a>
  <a href="mailto:sakabuana.pa@gmail.com">
  <img src="https://img.shields.io/badge/-Email-c14438?style=flat-square&logo=Gmail&logoColor=white" height="25px" alt="Email Badge">
  </a>
</div>

<h1 align="center">
  hey there
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
</h1>

### :dart: Goals :
> Learn to train, test, and deploy machine learing to predict salary based on years of experience

### :newspaper: Step :
1. To run in terminal first acitave env and run `conda activate env'
2. Install dependencies using `pip install -r requirements.txt`
3. Train and test the models with run `python3 models/regression.py` and save the output in pickel format [model.pkl](ml-regression-flask/models/pickled/model.pkl)
4. After that use the trained model and run `python3 server/regression.py` then you will get the output bellow

    ![terminal.png](ml-regression-flask/screenshoot/terminal.png)

5. Beside of that method we can use docker with run `docker-compose up --build -d` then you will get the output bellow

    ![docker.png](ml-regression-flask/screenshoot/docker.png)
    
6. Open this url on browser `http://127.0.0.1:5001/predict-salary?exp=12` and change values "12" with your desire number to predict the salary
7. In 100 years of experience it will get salary prediction below

    ![result.png](ml-regression-flask/screenshoot/result.png)