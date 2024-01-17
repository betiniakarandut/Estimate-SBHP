import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import './Results.css';

export const Results = () => {
  const [errorMessage, setErrorMessage] = useState(null);
  const location = useLocation();
  console.log('This is the entire location object:', location);
  const { estimate } = location?.state || {}
  console.log('This is estimate from Results:', estimate)

  let staticBHPResult;

  try {
    staticBHPResult = estimate.static_bhp_result;
  } catch (error) {
    console.error('Error accessing static_bhp_result:', error);
    setErrorMessage("Error: The result is not visible. Ensure that the input fields have met all the requirements.");
  }

  return (
    <div>
      <h2>Calculation Results</h2>
      <div className='pa1 ba br4 bw1'>
        <div className='sbhp dark-black ma2'>
          {errorMessage ? (
            <p className='error-message'>{errorMessage}</p>
          ) : (
            staticBHPResult
          )}
        </div>
        <div className='div1 pa1 ba br4 bw2'>
          <p className='k h2 white'>Some Useful Hints:</p>
          <p className='k h2'>Pseudo-critical pressure: {estimate.ppc_natural_gas_systems}</p>
          <p className='k h2'>Pseudo-critical temperature: {estimate.tpc_natural_gas_systems}</p>
          <p className='k h2'>Pseudo-reduced pressure: {estimate.reduced_pressure }</p>
          <p className='k h2'>Pseudo-reduced temperature: {estimate.reduced_temp}</p>
        </div>
      </div>
    </div>
  );
};
