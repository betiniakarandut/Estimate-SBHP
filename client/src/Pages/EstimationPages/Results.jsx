import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './Results.css';

export const Results = () => {
  const [errorMessage, setErrorMessage] = useState(null);
  const navigate = useNavigate();
  const location = useLocation();
  const { estimate } = location?.state || {};

  useEffect(() => {
    if (!estimate) {
      console.error('Estimation data not found in location state.');
      navigate('/home'); // Redirect to home if estimation data is not available
    }
  }, [estimate, navigate]);

  let staticBHPResult;

  try {
    staticBHPResult = estimate.static_bhp_result;
  } catch (error) {
    console.error('Error accessing static_bhp_result:', error);
    setErrorMessage(
      'Error 101: The result is not visible. Ensure that the input fields have met all the requirements.'
    );
  }

  return (
    <div>
      <div className="ki">
        <h2>Calculation Results</h2>
      </div>
      <div className="kii pa1 ba br4 bw4 ml6 mr6 mb4">
        <div className="sbhp ml7 center dark-black ma2">
          {errorMessage ? (
            <p className="error-message">{errorMessage}</p>
          ) : (
            staticBHPResult
          )}
        </div>
        <div className="div1 center pa1 ml-auto ba br4 bw2">
          <p className="k h2 white">Some Useful Hints:</p>
          <p className="k h3">Pseudo-critical pressure: {estimate.ppc_natural_gas_systems}</p>
          <p className="k h3">Pseudo-critical temperature: {estimate.tpc_natural_gas_systems}</p>
          <p className="k h3">Pseudo-reduced pressure: {estimate.reduced_pressure}</p>
          <p className="k h3">Pseudo-reduced temperature: {estimate.reduced_temp}</p>
        </div>
      </div>
    </div>
  );
};
