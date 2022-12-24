import React, { useState, useEffect } from 'react';
// import { Provider } from 'react-redux';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Index from './container';

// import some css here

function App() {
  return (
    <BrowserRouter>
      <div>
        navbar
      </div>
      <Routes>
        {/* <Route path="/" component={} /> */}
        <Route path="/" element={<Index />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App