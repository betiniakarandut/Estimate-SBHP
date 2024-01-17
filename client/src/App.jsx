import react from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { EstimateSbhp } from './Pages/EstimationPages/EstimateSbhp';
import { Results } from './Pages/EstimationPages/Results';
import './App.css'
import 'tachyons';


function App() {

  return (
    <>
      <div>
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
