import React, { useState, useEffect } from 'react';
// import { Provider } from 'react-redux';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Index from './container';
import Header from './component/ui/header';

// import some css here

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Index />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App