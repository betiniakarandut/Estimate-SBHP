import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Particles from 'react-tsparticles';
import { EstimateSbhp } from './Pages/EstimationPages/EstimateSbhp';
import { Results } from './Pages/EstimationPages/Results';
import { Login } from './Pages/LoginUser/Login';
import { Register } from './Pages/RegisterUser/Register';
import { Navigation } from './Components/Navigation';

const initialState = {
  user: {
    id: '',
    email: '',
  },
  route: 'signin',
  isloggedIn: false,
};

const App = () => {
  const [state, setState] = useState(initialState);

  const loadUser = (data) => {
    setState((prevState) => ({
      ...prevState,
      user: {
        id: data.id,
        email: data.email,
      },
      isloggedIn: true,
    }));
  };

  const onRouteChange = (route) => {
    if (route === 'logout') {
      setState(initialState);
    } else if (route === 'home') {
      setState((prevState) => ({ ...prevState, isloggedIn: true }));
    }
    setState((prevState) => ({ ...prevState, route: route }));
  };

  const { route, isloggedIn } = state;

  return (
    <div className="App">
      <Router>
        <Navigation isloggedIn={isloggedIn} onRouteChange={onRouteChange} />
        <Routes>
          <Route
            path="/"
            element={<Navigate to={isloggedIn ? '/home' : '/login'} />} // Redirect to '/home' if logged in
          />
          <Route
            path="/login"
            element={<Login loadUser={loadUser} onRouteChange={() => onRouteChange('home')} />}
          />
          <Route
            path="/register"
            element={<Register loadUser={loadUser} onRouteChange={() => onRouteChange('home')} />}
          />
          <Route path="/home" element={<EstimateSbhp />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;