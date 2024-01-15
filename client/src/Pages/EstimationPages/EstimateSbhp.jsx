import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { Cards } from '../../Components/Cards/Cards';

export const EstimateSbhp = () => {
  const [estimate, setEstimation] = useState({});
  const [formData, setFormData] = useState({
    well_depth: '',
    temp_avg_sys: '',
    gas_specific_gravity: '',
    static_wellhead_pressure: '',
  });

  const history = useHistory();

  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log({name : value})
    setFormData(prevState => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch("http://localhost:5000/api/calculate_properties", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          console.log("No data received");
        }
      })
      .then(data => {
        console.log(data);
        setEstimation(data);
        history.push('/results')
      })
      .catch(error => console.log("Error fetching data:", error));
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Well Depth:
          <input required type="text" name="well_depth" value={formData.well_depth} onChange={handleChange} />
        </label>
        <br />
        <label>
          Temp Avg Sys:
          <input required type="text" name="temp_avg_sys" value={formData.temp_avg_sys} onChange={handleChange} />
        </label>
        <br />
        <label>
          Gas Specific Gravity:
          <input required type="text" name="gas_specific_gravity" value={formData.gas_specific_gravity} onChange={handleChange} />
        </label>
        <br />
        <label>
          Static Wellhead Pressure:
          <input required type="text" name="static_wellhead_pressure" value={formData.static_wellhead_pressure} onChange={handleChange} />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
      <Cards />
    </div>
  );
};
