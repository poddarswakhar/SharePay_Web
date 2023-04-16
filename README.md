# SharePay_Web
Repository for SharePay DApp.

## Project Structure

This is the root of the project.

<li> backend: contains the backend code, solidity code and the SQL Database </li>
<li> frontend: contains the frontend code for react framework </li>
<li> FinalReport.pdf: The report for the project according to the guidelines on the syllabus </li>
<li> PresentationSlides.pdf: The slides used for the presentation </li>
<li> Demo Video Link: https://youtu.be/EjDmkX4-83E </li>

<br></br>

## Technologies Used

<li> Django </li>
<li> React </li>
<li> Web3 </li>
<li> Infura </li>
<li> Eth Network </li>
<li> Solidity </li>

<br></br>

## Dependencies

<b><u> Backend </u></b>

<li> Python 3 Setup </li>
<li> PIP </li>
<li> Django </li>
<li> Django Rest Framework </li>
<li> Django Cors Headers </li>
<li> Web3 </li>
<li> Solcx </li>
<br></br>
<b><u> Frontend </u></b>
<li> NodeJS </li>
<li> Bootstrap </li>
<li> Reactstrap </li>
<li> Axios </li>

<br></br>

## Getting Started

Instructions on how to get the project up and running on a local machine for development and testing purposes.

### Prerequisites & Installing

Make sure all the Dependencies are installed. Use pip or npm to install those dependencies. For front end dependencies install them on the frontend root of the repo. Or if NodeJS and NPM is installed, you can do like the following example:

```
cd frontend
npm install
```

For Backend these commands might come handy

```
pip install django djangorestframework django-cors-headers
pip install web3
pip install py-solc-x
```

### Running

Once all the Prerequisites are done installing now we should be ready to run the webapp. First we will start the backend (make sure backend server runs at at port 8000)

```
cd backend
python manage.py runserver
```

Note: By any chance if shows migration error run this lines before

```
python manage.py makemigrations
python manage.py migrate
```

Now lets start the front end at a different port

```
cd frontend
npm start
```

The project should be running with all the features, if any support is needed to get it started please do contact me at spoddar@student.ubc.ca or open an issue on the repo.

### Documentation
The Final report can be found on the root also
