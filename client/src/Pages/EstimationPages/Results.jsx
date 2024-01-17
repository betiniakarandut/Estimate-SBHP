import React from 'react';
import { useLocation } from 'react-router-dom';

export const Results = () => {
  const location = useLocation();
  console.log('This is the entire location object:', location);
  const { estimate } = location?.state || {}
  console.log('This is estimate from Results:',estimate)

  return (
    <div>
      <h2>Calculation Results</h2>
      <div>
        <p>Pseudocritical pressure: {estimate.ppc_natural_gas_systems}</p>
        <p>Pseudocritical temperature: {estimate.tpc_natural_gas_systems}</p>
        <p>Pseudo-reduced pressure: {estimate.reduced_pressure }</p>
        <p>Pseudo-reduced temperature: {estimate.reduced_temp}</p>
        <p>Static BHP: {estimate.static_bhp_result}</p>
      </div>
    </div>
  );
};