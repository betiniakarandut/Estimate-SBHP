import react, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { EstimateSbhp } from './Pages/EstimationPages/EstimateSbhp';
import { Results } from './Pages/EstimationPages/Results';
import './App.css'


function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <Router>
          <Switch>
            <Route path='/results' component={Results}/>
            <Route path='/' component={EstimateSbhp}/>
          </Switch>
        </Router>
        <EstimateSbhp/>
        {/* <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button> */}
      </div>
    </>
  )
}

export default App
