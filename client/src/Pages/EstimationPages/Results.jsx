import React from 'react';

export const Results = ({ estimate }) => {
  console.log(estimate);

  return (
    <div>
      {/* Display the results in the way you want */}
      <p>Result: {estimate.static_bhp_result}</p>
      {/* Add more UI elements to display other properties if needed */}
    </div>
  );
};