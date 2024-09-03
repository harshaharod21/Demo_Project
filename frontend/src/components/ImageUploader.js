import React, { useState } from 'react';

const ImageUploader = ({ onImagesChange }) => {
  const [uploadedFiles, setUploadedFiles] = useState([]);

  const handleFileChange = (event) => {
    const filesArray = Array.from(event.target.files);
    setUploadedFiles(filesArray);
    onImagesChange(filesArray);
  };

  return (
    <div>
      <input
        type="file"
        multiple
        accept="image/*"
        onChange={handleFileChange}
      />
      <div style={{ marginTop: '10px' }}>
        {uploadedFiles.length > 0 ? (
          <div>
            <p>{uploadedFiles.length} image(s) uploaded:</p>
            <ul>
              {uploadedFiles.map((file, index) => (
                <li key={index}>{file.name}</li>
              ))}
            </ul>
          </div>
        ) : (
          <p>No images uploaded yet.</p>
        )}
      </div>
    </div>
  );
};

export default ImageUploader;
