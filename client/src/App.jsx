import react from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { EstimateSbhp } from './Pages/EstimationPages/EstimateSbhp';
import { Results } from './Pages/EstimationPages/Results';
import Particles from "react-tsparticles";
import './App.css'


const particleParams = {
  fpsLimit: 60,
  particles: {
      color: {
        value: "#1DA9D1"
      },
      number: {
        density: {
          enable: true,
          value_area: 900
        },
        value: 200
      },
      opacity: {
        value: 1,
        random: false,
        anim: {
          enable: true,
          speed: 3,
          opacity_min: 0.5
        }
      },
      shape: {
        type: "star",
        color: "#000000"
      },
      size: {
        random: true,
        value: 30,
        anim: {
          enable: true,
          speed: 10,
          sync: false
        }
      },
      move: {
        enable: true,
        speed: 1,
        direction: "none",
        attract: {
          enable: false,
          rotateX: 800,
          rotateY: 1200
        }
      }
    },
    retina_detect: true
};
      

function App() {

  return (
    <>
      <div className='App'>
        <Particles 
          className='particles'
          params={particleParams}
        />
        <Router>
          <Routes>
            <Route path='/' element={<EstimateSbhp />}/>
            <Route path='/results' element={<Results />}/>
          </Routes>
        </Router>
      </div>
    </>
  )
}

export default App
