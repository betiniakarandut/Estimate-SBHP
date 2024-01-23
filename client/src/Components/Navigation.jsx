import React from 'react';
import { Link } from 'react-router-dom';

export const Navigation = ({ onRouteChange, isloggedIn }) => {
  const handleSignOut = () => {
    onRouteChange('logout');
  };

  return (
    <nav style={{ display: 'flex', justifyContent: 'flex-end' }}>
      {isloggedIn ? (
        <p onClick={handleSignOut} className="f3 link dim white underline pa3 pointer">
          Sign Out
        </p>
      ) : (
        <>
          <Link to="/login" className="f3 link dim white underline pa3 pointer">
            Sign In
          </Link>
          <Link to="/register" className="f3 link dim white underline pa3 pointer">
            Register
          </Link>
        </>
      )}
    </nav>
  );
};
