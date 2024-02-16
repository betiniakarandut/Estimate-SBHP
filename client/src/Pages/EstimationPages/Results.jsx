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
    if (estimate.static_bhp_result !== 200){
      console.error('Error accessing static_bhp_result:', error);
      setErrorMessage(
      'Error 101: The result is not visible. Ensure that the input fields have met all the requirements.'
      );
    }
    staticBHPResult = estimate.static_bhp_result;
  } catch (error) {
    console.error('Error accessing static_bhp_result:', error);
    setErrorMessage(
      'Error 101: The result is not visible. Ensure that the input fields have met all the requirements.'
    );
  }

  return (
    <div>
      <div className="kii pa1 bg-yellow ba br4 bw4 ml6 mr6 mb4">
        <div className="sbhp ml7 center dark-black ma2">
          {errorMessage ? (
            <p className="error-message">{errorMessage}</p>
          ) : (
            staticBHPResult
          )}
        </div>
        <div className="div1 center pa1 ml-auto ba br4 bw2">
          <p className="k h2 black">Some Useful Hints:</p>
          <p className="k h3">Pseudo-critical pressure, Ppc: {estimate.ppc_natural_gas_systems}</p>
          <p className="k h3">Pseudo-critical temperature, Tpc: {estimate.tpc_natural_gas_systems}</p>
          <p className="k h3">Pseudo-reduced pressure, Ppr: {estimate.reduced_pressure}</p>
          <p className="k h3">Pseudo-reduced temperature, Tpr: {estimate.reduced_temp}</p>
        </div>
      </div>
    </div>
  );
};
