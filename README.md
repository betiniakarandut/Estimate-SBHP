<div align="center">
  <h2><b>Estimate-SBHP</b></h2>
</div>

<!-- PROJECT DESCRIPTION -->
# 📖 Estimate-SBHP <a name="about-project"></a>
<div>
    This is my Final Year undergraduate project in partial fulfilment for the award of Bachelor of Engineering Degree in Chemical Engineering.
    During one of our lectures in the first semester Fourth Year, I learnt Natural Gas Engineering. Of the many methods of predicting/estimating static bottom hole pressure, I discovered that Sukkar and Cornell is widely used both for vertical and inclined wells especially for pressures below 10,000psia. 
    This model is made to relief reservoir engineers(or student engineers) who which to predict SBHP with the Sukkar and Cornell approach. This model has 98% accuracy as compared to the measured SBHP(with gauge). It is made to extrapolate and interpolate values to obtain best pseudo reduced wellhead pressure value, and carry out all the possible iterations involved in the calculation automatically.
    It is a light weight application built with Python3-Flask(backend) and React-Vite(frontend).
    
</div>
<br>

# 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

- Python3
- Flask
- React-Vite
- Pandas
- NumPy
<br>

![Languages](https://img.shields.io/github/languages/top/betiniakarandut/Estimate-SBHP)
![GitHub repo size](https://img.shields.io/github/repo-size/betiniakarandut/Estimate-SBHP)
![GitHub issues](https://img.shields.io/github/issues/betiniakarandut/Estimate-SBHP)
![GitHub closed issues](https://img.shields.io/github/issues-closed/betiniakarandut/Estimate-SBHP)
![GitHub](https://img.shields.io/github/license/betiniakarandut/Estimate-SBHP)
![GitHub Repo stars](https://img.shields.io/github/stars/betiniakarandut/Estimate-SBHP?style=social)


## Requirements
This Application requires:

**_Python (>= 3.9)_**<br>
**_numpy==1.23.2_**<br>
**_pandas==1.4.3_** <br>
**_Flask==3.0.0_**<br>
**_React-Vite_**<br>

See [Requirements](./server/requirements.txt) for details.

## <h2>Usage</h2>:

Visit the website at https://..................

<p><h2>Set your Environment Variables Below:</h2></p>
1. export SECRET_KEY=set to any random alphanumeric character or use python built-in `from uuid import uuid4()` to generate any random values<br>
2. export DB_PASSWORD = Betini2024
3. export REDIS_URL=redis://localhost:6379

<p><h2>Application and usage on the local machine</h2></p>
To use this application locally, follow the steps below:<br>
1.  Open the terminal or command prompt<br>
2.  git clone `<repo url>`<br>
3.  cd Estimate-SBHP<br>
4.  cd server<br>
5.  python3 views.py (use Postman to test the APIs)<br>
6.  cd client<br>
7.  npm install<br>
8.  npm run dev<br>
9.  visit `htpp://localhost:5173`

<p><h2>Application and usage Overview</h2></p>

<div>
  <div><p>Login Page</p>
    <p><img src="./Assets/login.png"/></p>
  </div>
  <div><p>Home Page</p>
    <p><img src="./Assets/homepage.png"/></p>
  </div>
  <div><p>Resutls Page</p>
    <p><img src="./Assets/resultspage.png"/></p>
  </div>
  

</div>

## Files :pencil:

| Property | Description |
|------|-------------|
| [server](./server) | Directory |
| [client](./client) | Directory |
| [README.md](./README.md) | File |




## Author

- Github: [betiniakarandut](https://www.github.com/betiniakarandut)
- LinkedIn: [betini-akarandut](https://www.linkedin.com/in/betini-akarandut-24654321a)
- Tweeter: [@betiniakarandut](https://twitter.com/betiniakarandut)
