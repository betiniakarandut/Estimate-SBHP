import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

export const Navigation = ({ onRouteChange, isloggedIn }) => {
  const navigate = useNavigate()
  const handleSignOut = () => {
    navigate('/');
    onRouteChange('logout');
  };

  return (
    <nav style={{ display: 'flex', justifyContent: 'flex-end' }}>
      {isloggedIn ? (
        <p onClick={handleSignOut} className="f3 link dim black grow underline mr4 pointer">
          Sign Out
        </p>
      ) : (
        <>
          <Link to="/login" className="f3 link dim black grow underline pa3 pointer">
            Sign In
          </Link>
          <Link to="/register" className="f3 link dim black grow underline pa3 pointer">
            Register
          </Link>
        </>
      )}
    </nav>
  );
};
