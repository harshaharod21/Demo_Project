import React, { useState } from 'react';

const TextContext = ({ onContextChange }) => {
  const handleChange = (event) => {
    onContextChange(event.target.value);
  };

  return (
    <textarea
      placeholder="Enter optional context here"
      onChange={handleChange}
    />
  );
};

export default TextContext;
