import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './EstimateSBHP.css';

export const EstimateSbhp = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    well_depth: '',
    temp_avg_sys: '',
    gas_specific_gravity: '',
    static_wellhead_pressure: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({ ...prevState, [name]: value }));
  };

  const handleEstimate = (e) => {
    e.preventDefault();

    fetch('https://sbhp-estimation.onrender.com/api/calculate_properties', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          console.log('No data received');
        }
      })
      .then((data) => {
        console.log(data);
        // Assuming 'data' contains the required estimation details
        navigate('/results', { state: { estimate: data } });
      })
      .catch((error) => console.log('Error fetching data:', error));
  };


  return (
    <div>
      <div className='gen pa2 f3 bg-red br4 ml5 mr5 fw-bold'>
				{'Please note that this model works for pressures below 10,000 psia. Give it a try!'}
			</div>
      <div className='form ba br4 bw2 ml6 mr6 mt1'>
        <form onSubmit={handleEstimate}>
          <label className='well-depth db mv2 mr-2 ml-auto'>
            <span className='b mr3 ok'>Well Depth:</span>
            <input 
              className="input-reset ba bw2 f50 b--black-50 br2 h2 center glow-on-hover f3 fw-bold " 
              required 
              type="text" 
              name="well_depth" 
              value={formData.well_depth} 
              onChange={handleChange} 
            />
          </label>
          <br />
          <label className='temp db mv2'>
            <span className='b mr3 ok'>Avg System Temp:</span>
            <input 
              className="input-reset bw2 ba b--black-50 br2 h2 glow-on-hover f3 fw-bold"  
              required 
              type="text" 
              name="temp_avg_sys" 
              value={formData.temp_avg_sys} 
              onChange={handleChange} 
            />
          </label>
          <br />
          <label className='spg db mv2'>
            <span className='b mr3 ok'>Gas Specific Gravity:</span>
            <input 
              className="input-reset ba bw2 b--black-50 br2 h2 glow-on-hover f3 fw-bold" 
              required 
              type="text" 
              name="gas_specific_gravity" 
              value={formData.gas_specific_gravity} 
              onChange={handleChange} 
            />
          </label>
          <br />
          <label className='wellhead db mv2'>
            <span className='b mr3 ok'>Static Wellhead Pressure:</span>
            <input 
              className="input-reset ba bw2 b--black-50 br2 h2 glow-on-hover f3 fw-bold" 
              required 
              type="text" 
              name="static_wellhead_pressure" 
              value={formData.static_wellhead_pressure} 
              onChange={handleChange} />
          </label>
          <br />
          <button className='btn br3 f4 grow link bg-light-purple shadow-5' type="submit">Estimate</button>
        </form>
      </div>
    </div>
  );
};
