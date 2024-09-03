import React, { useState } from 'react';
import ImageUploader from './components/ImageUploader';
import TextContext from './components/TextContext';
import DescribeButton from './components/DescribeButton';
import Markdown from 'markdown-to-jsx';  // Import markdown-to-jsx
import './styles.css';

const App = () => {
  const [images, setImages] = useState([]);
  const [context, setContext] = useState('');
  const [description, setDescription] = useState('');

  const handleImagesChange = (files) => {
    setImages(files);
  };

  const handleContextChange = (text) => {
    setContext(text);
  };

  const handleDescribe = async () => {
    const formData = new FormData();
    for (let i = 0; i < images.length; i++) {
      formData.append('images', images[i]);
    }
    formData.append('context', context);

    try {
      const response = await fetch('http://127.0.0.1:5000/describe', {  
        method: 'POST',
        body: formData,
      });
      const result = await response.json();
      setDescription(result.description);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="app-container">
      <h1>Feature Description Generator</h1>
      
      {/* Image Uploader Component */}
      <div className="file-upload">
        <ImageUploader onImagesChange={handleImagesChange} />
      </div>
      
      {/* Text Context Component */}
      <div>
        <TextContext onContextChange={handleContextChange} />
      </div>
      
      {/* Describe Button Component */}
      <div>
        <DescribeButton onDescribe={handleDescribe} />
      </div>

      {/* Description Output */}
      {description && (
        <div className="description-output">
          <h2>Description:</h2>
          <Markdown>{description}</Markdown> {/* Render Markdown as HTML */}
        </div>
      )}
    </div>
  );
};

export default App;
