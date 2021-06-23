# Automatic-Stock-Portfolio-Generator
Creates a stock portfolio based on you risk level, period of investment, and investment value


## App Website: 
https://automatic-stock-portfolio.herokuapp.com/


## To Run Locally

### Activate the Env

```
source venv/Scripts/activate
```

### Install the requirements

```
pip3 install -r requirements.txt
```


### Run The Server

```
python manage.py runserver
```


## What it does
My app gets input such as stock name, investment value, risk level, etc. to generate a stock portfolio. Furthermore, the app uses the Expert.ai API and yahoo-finance API to determine the sentiment of the general market and the specific stock. This will allow users to be more informed before investing