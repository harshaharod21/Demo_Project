import React from 'react';

const DescribeButton = ({ onDescribe }) => {
  return (
    <button onClick={onDescribe}>
      Describe Features
    </button>
  );
};

export default DescribeButton;
